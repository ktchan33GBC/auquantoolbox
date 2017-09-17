from backtester.features.feature import Feature


class MovingSDevFeature(Feature):

    @classmethod
    def computeForInstrument(cls, featureParams, featureKey, instrumentManager):
        instrumentLookbackData = instrumentManager.getLookbackInstrumentFeatures()
        data = instrumentLookbackData.getDataForFeatureForAllInstruments(featureParams['featureName'])
        sdev = data[-featureParams['period']:].std()
        return sdev

    @classmethod
    def computeForMarket(cls, featureParams, featureKey, currentMarketFeatures, instrumentManager):
        lookbackDataDf = instrumentManager.getDataDf()
        data = lookbackDataDf[featureParams['featureName']]
        sdev = data[-featureParams['period']:].std()
        if len(data) < 1:
            return 0
        return sdev
