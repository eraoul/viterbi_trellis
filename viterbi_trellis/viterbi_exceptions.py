# Exceptions for viterbi_trellis library


class ViterbiTrellisException(Exception):
    """Base exception class for the viterbi_trellis library."""
    pass


class ViterbiTrellisEmptyLayerException(ViterbiTrellisException):
    """Raised when there is an empty layer in the trellis."""
    pass
