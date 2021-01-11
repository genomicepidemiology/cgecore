from cge2.applications.command import _ContentArgument, CommandLineBase
from cge2.applications.command import _SwitchArgument


class _BlastBaseCommandline(CommandLineBase):
    """Base Commandline object for Blast wrappers (PRIVATE).
    This is provided for subclassing, it deals with shared options
    common to all the blast tools (blastn, etc).
    """

    def __init__(self, cmd=None, path_exec="", **kwargs):
        assert cmd is not None
        extra_parameters = [
            # Core:
            _SwitchArgument(
                ["-h", "help"],
                "Print USAGE, DESCRIPTION description; "
                "ignore other arguments.",
                no_run=True,
            ),
            _SwitchArgument(
                ["-help", "help_extended"],
                "Print EXTENDED USAGE, DESCRIPTION and ARGUMENTS description; "
                "ignore other arguments.",
                no_run=True,
            ),
            _SwitchArgument(
                ["-version", "version"],
                "Print version number;  "
                "ignore other arguments.",
                no_run=True,
            ),
            _ContentArgument(
                ["", "custom_args"],
                "Add custom arguments that are not included in the "
                "kma_application.py file."
            ),
        ]
        try:
            # Insert extra parameters - at the start just in case there
            # are any arguments which must come last:
            self.parameters = extra_parameters + self.parameters
        except AttributeError:
            # Should we raise an error?  The subclass should have set this up!
            self.parameters = extra_parameters
        # Do we need a method to add a method for adding arguments in front?
        CommandLineBase.__init__(self, cmd, path_exec, **kwargs)

    def _validate_incompatibilities(self, incompatibles):
        """Validate parameters for incompatibilities (PRIVATE).
        Used by the _validate method.
        """
        for a in incompatibles:
            if self._get_parameter(a):
                for b in incompatibles[a]:
                    if self._get_parameter(b):
                        raise ValueError("Options %s and %s are incompatible."
                                         % (a, b))
