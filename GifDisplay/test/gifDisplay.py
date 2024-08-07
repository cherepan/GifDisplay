import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')
options.register('plotdir', '', mytype=VarParsing.varType.string)
options.parseArguments()
process = cms.Process("GifDisplay")

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load("Configuration/Geometry/GeometryIdeal2015Reco_cff")
#process.load("Configuration/Geometry/IdealGeometry_cff")
#process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("RecoMuon.MuonSeedGenerator.standAloneMuonSeeds_cff")
#process.load("RecoMuon.GlobalMuonProducer.globalMuons_cff")

#process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v0'


MCGlobalTag='124X_mcRun3_2022_realistic_v12' #for DYmumu_PU140
#DataGlobalTag='76X_dataRun2_v19'
#DataGlobalTag='76X_dataRun2_v15'
#DataGlobalTag='92X_dataRun2_Prompt_v11'
#DataGlobalTag='106X_dataRun2_v32'
DataGlobalTag='124X_dataRun3_PromptAnalysis_v1'



process.GlobalTag.globaltag=MCGlobalTag





#process.options = cms.untracked.PSet(
#	SkipEvent = cms.untracked.vstring('LogicError','ProductNotFound')
#)


process.MessageLogger = cms.Service("MessageLogger",
       destinations   = cms.untracked.vstring('myDebugOutputFile.txt'),
       debugModules = cms.untracked.vstring('*'),
       message = cms.untracked.PSet(
                                   threshold = cms.untracked.vstring('DEBUG')
                                   )
)


#pickEvent = '284036:439337726'
#pickEvent = '284036:439691998'
pickEvent = '284036:173346539'
process.source = cms.Source("PoolSource",
#  fileNames = cms.untracked.vstring('file:me11_test27_oct23.root')

                            
#  fileNames = cms.untracked.vstring('file:pickevents_26.root') #../../inputRoot/0026F566-83BB-E711-B677-7845C4FC3683.root')
  fileNames = cms.untracked.vstring('file:SingleMu10Pt_100_TestEvents_AddUFLocalREco_1.root')



                            
#        /store/user/cherepan/RelValZMM_14/RelValMM14_ReRunLocalReco/230927_095118/0000/SingleMu10Pt_100_TestEvents_AddUFLocalREco_1.root
#  fileNames = cms.untracked.vstring('file:Zmu_rawreco_2016H.root') #../../inputRoot/0026F566-83BB-E711-B677-7845C4FC3683.root')

#  fileNames = cms.untracked.vstring('file:../../inputRoot/Zmu_rawreco_2016H.root')
#  eventsToProcess = cms.untracked.VEventRange(pickEvent + '-' + pickEvent)

)

maxEvents = cms.untracked.PSet(
     input = cms.untracked.int32(-1)
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.GifDisplay = cms.EDAnalyzer('GifDisplay',
#rootFileName = cms.untracked.string("output_me11_test27_oct30.root"),
rootFileName = cms.untracked.string("output.root"),

stripDigiTagSrc = cms.untracked.InputTag("muonCSCDigis","MuonCSCStripDigi"),
wireDigiTagSrc = cms.untracked.InputTag("muonCSCDigis","MuonCSCWireDigi"),
                                    
compDigiTagSrc = cms.untracked.InputTag("muonCSCDigis", "MuonCSCComparatorDigi"),
                                    
alctDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCALCTDigi'),
clctDigiTagSrc = cms.untracked.InputTag('muonCSCDigis', 'MuonCSCCLCTDigi'),

#MuonDigiCollection<CSCDetId,CSCStripDigi>    "muonCSCDigis"              "MuonCSCStripDigi"   "localRecoUF"
#MuonDigiCollection<CSCDetId,CSCWireDigi>    "muonCSCDigis"              "MuonCSCWireDigi"   "localRecoUF"


                                    
#cscRecHitTag = cms.InputTag("csc2DRecHits",""),

#corrlctDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCCorrelatedLCTDigi'),  # unused 


                                    
#directory for eventdisplay
eventDisplayDir = cms.untracked.string(options.plotdir),
#eventDisplayDir = cms.untracked.string("/home/mhl/public_html/2017/20171201_cscSeg/"),
#chamber type: ME1/1-11, ME2/1-21
chamberType = cms.untracked.string('21')
)


process.p = cms.Path(process.muonCSCDigis  * process.GifDisplay)
