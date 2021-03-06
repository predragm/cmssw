import FWCore.ParameterSet.Config as cms

OutALCARECOSiPixelLorentzAngle_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiPixelLorentzAngle')
    ),
    outputCommands = cms.untracked.vstring(
        'keep *_globalMuons_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*', 
        'drop *_*_*_HLT')
)

import copy

OutALCARECOSiPixelLorentzAngle=copy.deepcopy(OutALCARECOSiPixelLorentzAngle_noDrop)
OutALCARECOSiPixelLorentzAngle.outputCommands.insert(0, "drop *")
