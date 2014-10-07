import mock

from twisted.trial.unittest import TestCase

from allmydata.web.common import get_filenode_metadata, SDMF_VERSION, MDMF_VERSION

class TestGetFileNodeMetaData(TestCase):
    def test_size_not_None(self):
        mockfilenode = mock.Mock()
        mockfilenode.get_version.return_value = SDMF_VERSION
        metadata = get_filenode_metadata(mockfilenode)
        self.failUnlessIsInstance(metadata, dict)
