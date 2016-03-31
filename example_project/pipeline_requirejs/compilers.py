from pipeline.compilers import SubProcessCompiler, CompilerError
from django.conf import settings

from logging import getLogger
log = getLogger('development')

class RequireCompiler(SubProcessCompiler):

    output_extension = 'optimised.js'

    def match_file(self, filename):
        return filename.endswith('.js')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        log.debug('infile: %s' % infile)
        log.debug('outfile: %s' % outfile)
        if not outdated and not force:
            return # No need to recompile the file

        # Execute the command
        command = "%s -o %s out=%s" % (getattr(settings, 'PIPELINE_REQUIREJS_BINARY', 'r.js'), infile, outfile)

        return self.execute_command(command)