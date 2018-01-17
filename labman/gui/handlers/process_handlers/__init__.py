# ----------------------------------------------------------------------------
# Copyright (c) 2017-, labman development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .sample_plating_process import (
    SamplePlatingProcessListHandler, SamplePlatingProcessHandler)
from .gdna_extraction_process import GDNAExtractionProcessHandler
from .library_prep_16s_process import LibraryPrep16SProcessHandler
from .quantification_process import (
    QuantificationProcessParseHandler, QuantificationProcessHandler)
from .pooling_process import (
    PoolPoolProcessHandler, LibraryPoolProcessHandler)
from .sequencing_process import (
    SequencingProcessHandler, DownloadSampleSheetHandler)

__all__ = ['SamplePlatingProcessListHandler', 'SamplePlatingProcessHandler',
           'GDNAExtractionProcessHandler', 'LibraryPrep16SProcessHandler',
           'QuantificationProcessParseHandler', 'QuantificationProcessHandler',
           'PoolPoolProcessHandler', 'LibraryPoolProcessHandler',
           'SequencingProcessHandler', 'DownloadSampleSheetHandler']

PROCESS_ENDPOINTS = [
    (r"/process/sample_plating/([0-9]+)$", SamplePlatingProcessHandler),
    (r"/process/sample_plating$", SamplePlatingProcessListHandler),
    (r"/process/gdna_extraction$", GDNAExtractionProcessHandler),
    (r"/process/library_prep_16S$", LibraryPrep16SProcessHandler),
    (r"/process/parse_quantify$", QuantificationProcessParseHandler),
    (r"/process/quantify$", QuantificationProcessHandler),
    (r"/process/poolpools$", PoolPoolProcessHandler),
    (r"/process/poollibraries$", LibraryPoolProcessHandler),
    (r"/process/sequencing$", SequencingProcessHandler),
    (r"/process/sequencing/([0-9]+)/sample_sheet$", DownloadSampleSheetHandler)
]
