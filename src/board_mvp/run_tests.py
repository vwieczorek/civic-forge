import sys
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))

from board_mvp.tests import test_schema, test_api, test_web


def run():
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        test_schema.test_schema_creation(tmp_path=tmp_path)
        test_api.test_quest_lifecycle(tmp_path=tmp_path)
        test_api.test_decay(tmp_path=tmp_path)
        test_api.test_multiple_decay_runs(tmp_path=tmp_path)
        test_web.test_web_forms(tmp_path=tmp_path)
    print('All tests passed.')


if __name__ == '__main__':
    run()
