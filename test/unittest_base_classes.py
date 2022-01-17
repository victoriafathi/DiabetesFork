import unittest


class TestAbstractClasses(unittest.TestCase):

    # Test that BaseMetric is an abstract class with two methods evaluate() and get_name()
    def test_base_metric(self):
        from model.metrics.base_metric import BaseMetric
        self.assertRaises(TypeError, BaseMetric)

        class ImplementedMetric(BaseMetric):

            def evaluate(self, ground_truth, prediction):
                pass

            def get_name(self):
                return "name"
        self.assertEqual(ImplementedMetric().get_name(), "name")

    # Test that BaseModel is an abstract class with three methods predict(), fit() and get_name()
    def test_base_model(self):
        from model.models.base_model import BaseModel
        self.assertRaises(TypeError, BaseModel)

        class ImplementedModel(BaseModel):

            def predict(self, x):
                pass

            def fit(self, data):
                pass

            def get_name(self):
                return "name"

        self.assertEqual(ImplementedModel().get_name(), "name")

    # Test that BaseExtractor is an abstract class with three methods extract(), get_name() and get_params()
    def test_base_extractor(self):
        from model.etl.extract.base_exractor import BaseExtractor
        self.assertRaises(TypeError, BaseExtractor)

        class ImplementedExtractor(BaseExtractor):

            def extract(self, data):
                pass

            def get_name(self):
                return "name"

            def get_params(self):
                return {"dir": "data"}

        self.assertEqual(ImplementedExtractor().get_name(), "name")
        self.assertEqual(ImplementedExtractor().get_params()["dir"], "data")

    # Test that BaseTransformer is an abstract class with three methods apply(), get_name() and get_params()
    def test_base_transformer(self):
        from model.etl.transform.base_transformer import BaseTransformer
        self.assertRaises(TypeError, BaseTransformer)

        class ImplementedTransformer(BaseTransformer):

            def apply(self, x):
                pass

            def get_name(self):
                return "name"

            def get_params(self):
                return {"alpha": 1}

        self.assertEqual(ImplementedTransformer().get_name(), "name")
        self.assertEqual(ImplementedTransformer().get_params()["alpha"], 1)

    # Test that BaseETL is an abstract class with three methods _load_case(), get_name() and get_params()
    def test_base_etl_pipeliene(self):

        from model.etl.base_etl import BaseETL
        self.assertRaises(TypeError, BaseETL)

        class ImplementedETL(BaseETL):

            def _load_case(self, x):
                pass

            def get_name(self):
                return "name"

            def get_params(self):
                return {"batch_size": 32}

        self.assertEqual(ImplementedETL().get_name(), "name")
        self.assertEqual(ImplementedETL().get_params()["batch_size"], 32)

    # Test that SimpleETL is an abstract class with four methods load(), _load_case(), get_name() and get_params()
    def test_simple_etl_pipeliene(self):

        from model.etl.base_etl import SimpleETL
        self.assertRaises(TypeError, SimpleETL)

        class ImplementedETL(SimpleETL):
            
            def load(self):
                pass

            def _load_case(self, x):
                pass

            def get_name(self):
                return "name"

            def get_params(self):
                return {"batch_size": 32}

        self.assertEqual(ImplementedETL().get_name(), "name")
        self.assertEqual(ImplementedETL().get_params()["batch_size"], 32)

    # Test that BaseTrainValidationETL is an abstract class with five methods load_train(), load_validation(), _load_case(), get_name() and get_params()
    def test_train_val_etl_pipeliene(self):

        from model.etl.base_etl import BaseTrainValidationETL
        self.assertRaises(TypeError, BaseTrainValidationETL)

        class ImplementedETL(BaseTrainValidationETL):
            
            def load_train(self):
                pass

            def load_validation(self):
                pass

            def _load_case(self, x):
                pass

            def get_name(self):
                return "name"

            def get_params(self):
                return {"batch_size": 32}

        self.assertEqual(ImplementedETL().get_name(), "name")
        self.assertEqual(ImplementedETL().get_params()["batch_size"], 32)

    # Test that CrossValidationETL is an abstract class with five methods get_folds(), load_data(), _load_case(), get_name() and get_params()
    def test_cv_etl_pipeliene(self):

        from model.etl.base_etl import CrossValidationETL
        self.assertRaises(TypeError, CrossValidationETL)

        class ImplementedETL(CrossValidationETL):
            
            def get_folds(self):
                pass

            def load_data(self, fold):
                pass

            def _load_case(self, x):
                pass

            def get_name(self):
                return "name"

            def get_params(self):
                return {"batch_size": 32}

        self.assertEqual(ImplementedETL().get_name(), "name")
        self.assertEqual(ImplementedETL().get_params()["batch_size"], 32)

    # Test that BaseReporter is an abstract class with three methods report_metric(), add_plot() and report_plots()
    def test_base_reporter(self):
        from model.reporting.base_reporter import BaseReporter
        self.assertRaises(TypeError, BaseReporter)

        class ImplementedReporter(BaseReporter):
            
            def __init__(self):
                self.plots = []

            def report_metric(self, metric, value):
                return (metric, value)

            def add_plot(self, plot):
                self.plots.append(plot)

            def report_plots(self):
                return self.plots

        reporter = ImplementedReporter()
        self.assertEqual(reporter.report_metric("a", 1), ("a", 1))
        reporter.add_plot("plot")
        self.assertEqual(reporter.report_plots(), ["plot"])

    # Test that BasePlot is an abstract class with one method produce_plot()
    def test_base_plot(self):
        from model.reporting.plots.base_plot import BasePlot
        self.assertRaises(TypeError, BasePlot)

        class ImplementedPlot(BasePlot):
            
            def produce_plot(self):
                return "plot"

        self.assertEqual(ImplementedPlot().produce_plot(), "plot")

     # Test that ImagePlot is an abstract class with three methods produce_plot(), get_filename() and set_save_directory()
    def test_image_plot(self):
        from model.reporting.plots.base_plot import ImagePlot
        self.assertRaises(TypeError, ImagePlot)

        class ImplementedPlot(ImagePlot):
            
            def produce_plot(self):
                return "plot"
            
            def set_save_directory(self, directory):
                self.directory = directory
            
            def get_filename(self):
                return self.directory + "plot"

        plot = ImplementedPlot()
        self.assertEqual(plot.produce_plot(), "plot")
        plot.set_save_directory("dir/")
        self.assertEqual(plot.get_filename(), "dir/plot")
