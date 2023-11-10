import polars as pl

class PegaDefaultTables:
    class ADMModelSnapshot:
        pxApplication = pl.Categorical
        pyAppliesToClass = pl.Categorical
        pyModelID = pl.Utf8
        pyConfigurationName = pl.Categorical
        pySnapshotTime = pl.Datetime
        pyIssue = pl.Categorical
        pyGroup = pl.Categorical
        pyName = pl.Utf8
        pyChannel = pl.Categorical
        pyDirection = pl.Categorical
        pyTreatment = pl.Utf8
        pyPerformance = pl.Float64
        pySuccessRate = pl.Float64
        pyResponseCount = pl.Float32
        pxObjClass = pl.Categorical
        pzInsKey = pl.Utf8
        pxInsName = pl.Utf8
        pxSaveDateTime = pl.Datetime
        pxCommitDateTime = pl.Datetime
        pyExtension = pl.Utf8
        pyActivePredictors = pl.UInt16
        pyTotalPredictors = pl.UInt16
        pyNegatives = pl.Float32
        pyPositives = pl.Float32
        pyRelativeNegatives = pl.Float32
        pyRelativePositives = pl.Float32
        pyRelativeResponseCount = pl.Float32
        pyMemory = pl.Utf8
        pyPerformanceThreshold = pl.Float32
        pyCorrelationThreshold = pl.Float32
        pyPerformanceError = pl.Float32
        pyModelData = pl.Utf8
        pyModelVersion = pl.Utf8
        pyFactoryUpdatetime = pl.Datetime

    class ADMPredictorBinningSnapshot:
        pxCommitDateTime = pl.Datetime
        pxSaveDateTime = pl.Datetime
        pyModelID = pl.Utf8
        pxObjClass = pl.Categorical
        pzInsKey = pl.Utf8
        pxInsName = pl.Utf8
        pyPredictorName = pl.Categorical
        pyContents = pl.Utf8
        pyPerformance = pl.Float64
        pyPositives = pl.Float32
        pyNegatives = pl.Float32
        pyType = pl.Categorical
        pyTotalBins = pl.UInt16
        pyResponseCount = pl.Float32
        pyRelativePositives = pl.Float32
        pyRelativeNegatives = pl.Float32
        pyRelativeResponseCount = pl.Float32
        pyBinNegatives = pl.Float32
        pyBinPositives = pl.Float32
        pyBinType = pl.Categorical
        pyBinNegativesPercentage = pl.Float32
        pyBinPositivesPercentage = pl.Float32
        pyBinSymbol = pl.Utf8
        pyBinLowerBound = pl.Float32
        pyBinUpperBound = pl.Float32
        pyRelativeBinPositives = pl.Float32
        pyRelativeBinNegatives = pl.Float32
        pyBinResponseCount = pl.Float32
        pyRelativeBinResponseCount = pl.Float32
        pyBinResponseCountPercentage = pl.Float32
        pySnapshotTime = pl.Datetime
        pyBinIndex = pl.UInt16
        pyLift = pl.Float64
        pyZRatio = pl.Float64
        pyEntryType = pl.Categorical
        pyExtension = pl.Utf8
        pyGroupIndex = pl.UInt16
        pyCorrelationPredictor = pl.Float32

    class pyValueFinder():
        pyDirection = pl.Categorical
        pySubjectType = pl.Categorical
        ModelPositives = pl.UInt32
        pyGroup = pl.Categorical
        pyPropensity = pl.Float64
        FinalPropensity = pl.Float64
        pyStage = pl.Categorical
        pxRank = pl.UInt16
        pxPriority = pl.Float64
        pyModelPropensity = pl.Float64
        pyChannel = pl.Categorical
        Value = pl.Float64
        pyName = pl.Utf8
        StartingEvidence = pl.UInt32
        pySubjectID = pl.Utf8
        DecisionTime = pl.Datetime
        pyTreatment = pl.Utf8
        pyIssue = pl.Categorical