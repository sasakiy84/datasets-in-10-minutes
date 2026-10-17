import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('build_site', Path(__file__).resolve().parents[1] / 'scripts/build_site.py')
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)


class CatalogDateTests(unittest.TestCase):
    def test_tracks_renames_and_both_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args, date=None):
                env = dict(os.environ)
                if date:
                    env.update(GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
                return subprocess.check_output(['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', *args], cwd=root, env=env, stderr=subprocess.DEVNULL)
            def commit(date):
                git('add', '.')
                git('commit', '-m', 'fixture', date=date)
            git('init')
            (root / 'old.pptx').write_text('original')
            commit('2020-01-01T00:00:00Z')
            git('mv', 'old.pptx', 'deck.pptx')
            (root / 'deck.pdf').write_text('pdf')
            commit('2021-01-01T00:00:00Z')
            (root / 'deck.pdf').write_text('updated pdf')
            commit('2022-01-01T00:00:00Z')
            (root / 'unrelated').write_text('unrelated metadata update')
            commit('2023-01-01T00:00:00Z')
            row = dict(slug='deck', pdf='deck.pdf', pptx='deck.pptx')
            with patch.object(site, 'ROOT', root):
                site.restore_dates(row)
            self.assertEqual(row['created_at'], '2020-01-01T00:00:00Z')
            self.assertEqual(row['updated_at'], '2022-01-01T00:00:00Z')

    def test_without_git_preserves_exported_metadata(self):
        row = dict(slug='deck', pdf='deck.pdf', pptx='deck.pptx', created_at='2020-01-01T09:00:00+09:00', updated_at='2022-01-01T00:00:00Z')
        with patch.object(site.subprocess, 'check_output', side_effect=FileNotFoundError):
            site.restore_dates(row)
        self.assertEqual(row['created_at'], '2020-01-01T00:00:00Z')
        self.assertEqual(row['updated_at'], '2022-01-01T00:00:00Z')

    def test_shallow_history_does_not_invent_creation_date(self):
        row = dict(slug='deck', pdf='deck.pdf', pptx='deck.pptx')
        def output(args, **kwargs):
            return 'true\n' if args[1] == 'rev-parse' else '2022-01-01T00:00:00Z\n'
        with patch.object(site.subprocess, 'check_output', side_effect=output):
            site.restore_dates(row)
        self.assertEqual(row['created_at'], '')
        self.assertEqual(row['updated_at'], '2022-01-01T00:00:00Z')

    def test_rejects_date_without_timezone(self):
        with self.assertRaises(ValueError):
            site.timestamp('2020-01-01T00:00:00')


if __name__ == '__main__':
    unittest.main()
