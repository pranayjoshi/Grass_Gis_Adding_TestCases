import unittest

import grass.pygrass.modules as gmodules

import grass.script as gscript







USE_VALGRIND = False





class GrassTestCase(unittest.TestCase):

    """Base class for GRASS test cases."""



    def run_module(self, module):

        """Method to run the module. It will probably use some class or instance variables"""

        # get command from pygrass module

        command = module.make_cmd()

        # run command using valgrind if desired and module is not python script

        # see also valgrind notes at be end of this section

        if is_not_python_script(command[0]) and USE_VALGRIND:

            command = ['valgrind', '--tool=...', '--xml=...', '--xml-file=...'] + command

        # run command

        # store valgrind output (memcheck has XML output to a file)

        # store module return code, stdout and stderr, how to distinguish from valgrind?

        # return code, stdout and stderr could be returned in tuple



    def assertRasterMap(self, actual, reference, msg=None):

        # e.g. g.compare.md5 from addons

        # uses msg if provided, generates its own if not,

        # or both if self.longMessage is True (unittest.TestCase.longMessage)

        # precision should be considered too (for FCELL and DCELL but perhaps also for CELL)



        if checksums == "":

            self.fail(...)  # unittest.TestCase.fail

    def g_region(self):

        """" To Validate the Output """

        # Configure a g.region raster='elevation' test



        module = gmodules.Module("g.region", raster = "elevation")



        self.run_module(module=module)

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")





class stream_slope_ModuleTestCase(GrassTestCase):

    def test_flag_overwrite(self):

        # Configure a r.stream.slope flag= "Overwrite" test



        module = gmodules.Module("r.stream.slope", direction='dir', elevation="elevation", gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="overwrite")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def test_flag_help(self):

        # Configure a r.stream.slope flag= "help" test



        module = gmodules.Module("r.stream.slope", elevation="elevation", direction='dir', gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="help")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def test_flag_verbose(self):

        # Configure a r.stream.slope flag= "verbose" test



        module = gmodules.Module("r.stream.slope", direction='dir', elevation="elevation", gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="verbose")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def test_flag_quiet(self):

        """" To Validate the Output """

        # Configure a r.stream.slope flag= "quiet" test



        module = gmodules.Module("r.stream.slope", direction='dir', elevation="elevation", gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="quiet")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def test_flag_ui(self):

        """" To Validate the Output """

        # Configure a r.stream.slope flag= "ui" test



        module = gmodules.Module("r.stream.slope", direction='dir', elevation="elevation", gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="ui")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")





    def setUp(self):

    # will raise import error which will cause error in test (as opposed to test failure)

        from scipy import something

    # save this for later user in test method(s)

        self.something = something



    def test_some_test(self):

        a = ...

        b = self.something(params, ...)

        self.assertEqual(a, b, "The a result differs from the result of the function from scipy")
