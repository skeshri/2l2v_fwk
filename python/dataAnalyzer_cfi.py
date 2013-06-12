import FWCore.ParameterSet.Config as cms

from CMGTools.External.pujetidproducer_cfi import pileupJetIdProducerChs
pileupJetIdProducerChs.algos[0].tmvaWeights=cms.string("CMGTools/External/data/TMVAClassificationCategory_JetID_53X_chs_Dec2012.weights.xml")  

                 
dataAnalyzer = cms.EDAnalyzer( "DataAnalyzer",
                               cfg=cms.PSet( metFilters=cms.vstring('HBHENoiseFilter',
                                                                    'hcalLaserEventFilter',
                                                                    'EcalDeadCellTriggerPrimitiveFilter',
                                                                    'eeBadScFilter',
                                                                    'ecalLaserCorrFilter',
                                                                    'trackingFailureFilter',
                                                                    'manystripclus53X',
                                                                    'toomanystripclus53X',
                                                                    'logErrorTooManyClusters'),
                                             triggerSource = cms.InputTag("TriggerResults::HLT"),
                                             triggerPaths = cms.vstring('Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v',
                                                                        'DoubleEle33_CaloIdL_GsfTrkIdVL_v',
                                                                        'Mu17_Mu8_v',
                                                                        'Mu17_TkMu8_v',
                                                                        'Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v',
                                                                        'Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v',
                                                                        'IsoMu24_eta2p1_v',
                                                                        'Photon36_R9Id90_HE10_Iso40_EBOnly_v',                  
                                                                        'Photon50_R9Id90_HE10_Iso40_EBOnly_v',
                                                                        'Photon75_R9Id90_HE10_Iso40_EBOnly_v',
                                                                        'Photon90_R9Id90_HE10_Iso40_EBOnly_v',
                                                                        'Photon250_NoHE_v1_v',
                                                                        'Photon300_NoHE_v1_v'),
                                             triggerCats  = cms.vint32(1111,
                                                                       1111,
                                                                       1313,
                                                                       1313,
                                                                       1113,
                                                                       1113,
                                                                       1313,
                                                                       22,
                                                                       22,
                                                                       22,
                                                                       22,
                                                                       22,
                                                                       22
                                                                       ),
                                             genSource       = cms.InputTag("genParticles"),
                                             vtxSource       = cms.InputTag("goodOfflinePrimaryVertices"),
                                             beamSpotSource  = cms.InputTag("offlineBeamSpot"),
                                             pfSource        = cms.InputTag("particleFlow"),
                                             muonSource      = cms.InputTag("selectedPatMuonsPFlow"),
                                             electronSource  = cms.InputTag("selectedPatElectronsPFlow"),
                                             photonSource    = cms.InputTag("photons"),
                                             conversionSource= cms.InputTag("allConversions"),
                                             ebrechitsSource = cms.InputTag("reducedEcalRecHitsEB"),
                                             eerechitsSource = cms.InputTag("reducedEcalRecHitsEE"),
                                             jetSource       = cms.InputTag("selectedPatJetsPFlow"),
                                             pujetidAlgo     = pileupJetIdProducerChs.algos,
                                             metSource       = cms.VInputTag("pfMETPFlow","pfMet","pfType1CorrectedMet","pfType1p2CorrectedMet"),
                                             rhoSource       = cms.InputTag("kt6PFJets:rho"),
                                             rho25Source      = cms.InputTag("kt6PFJetsCentral:rho")
                                             )
                               )

## configure specifically for a dijet analysis
dijetAnalyzer = dataAnalyzer.clone()
dijetAnalyzer.cfg.triggerPaths=cms.vstring("BTagMu_DiJet20","BTagMu_DiJet40","BTagMu_DiJet70","BTagMu_DiJet110","BTagMu_Jet300")
dijetAnalyzer.cfg.triggerCats=cms.vint32(1,1,1,1,1)
