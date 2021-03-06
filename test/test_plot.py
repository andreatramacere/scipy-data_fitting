import os
import test_fit

from scipy_data_fitting import Plot

class TestPlot():

    @classmethod
    def teardown_class(cls):
        path = 'test/test.svg'
        if os.path.exists(path): os.remove(path)

    def get_fit_for_fitting(self):
        return test_fit.TestFit().get_fit_for_fitting()

    def test_save(self):
        plot = Plot(fit=self.get_fit_for_fitting())
        plot.save('test/test.svg')
        assert os.path.exists('test/test.svg')
