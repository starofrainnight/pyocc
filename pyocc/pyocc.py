# -*- coding: utf-8 -*-

"""Main module."""

import os
import sys
import glob
import subprocess
import openccbinary as occbin
from whichcraft import which


class PyOCC(object):
    """OpenCC API class
    """

    def _guess_cfg_dir(self, executable):
        cfg_dir = os.path.dirname(executable)

        # Check if *.ocd files with executable ? That means configuration files
        # are in the same directory.
        if glob.glob(os.path.join(cfg_dir, '*.ocd')):
            return cfg_dir

        # The OpenCC may distribute as unix directory struct
        cfg_dir = os.path.join(os.path.dirname(cfg_dir), 'share/opencc')
        if glob.glob(os.path.join(cfg_dir, '*.ocd')):
            return cfg_dir

        raise FileNotFound("Can't find any opencc configuration files!")

    def __init__(self, executable=None):
        """Initialize OpenCC object

        :param executable: Specific OpenCC's binary path, search OpenCC or use
        the one provied by openccbinary package when set to None, defaults to
        None
        :param executable: str, optional
        """

        if not executable:
            if sys.platform.startswith('win32'):
                executable = occbin.executable
            else:
                executable = which('opencc')

        if not which(executable):
            raise FileNotFoundError(executable)

        self._executable = executable
        self._cfg_dir = self._guess_cfg_dir(executable)
        self._cfgs = None

    def convert(self, from_text, config):
        """Convert from text to required literal style of Chinese by specific
        configuration.

        :param from_text: The text you want to convert from
        :type from_text: str
        :param config: Convert configuration
        :type config: str
        """

        # We can't just pass the whole text to opencc, because the output
        # message will cut off at the line separator. That lead broken
        # translations.
        lines = from_text.splitlines()
        converted_lines = []
        for aline in lines:
            # If line is empty, we just add empty string to converted_lines
            if not aline:
                converted_lines.append('')
                continue

            converted_lines.append(subprocess.check_output(
                ['opencc', '-c', self._cfgs[config]],
                input=aline.encode('utf-8')).decode('utf-8'))
        return '\n'.join(converted_lines)

    def _config_to_new_style(self, config_name):
        """Convert an old style config name to new style

        :param config_name: Old style config name
        :type config_name: str
        :return: The new style config name
        :rtype: str
        """

        mappings = {
            'zhs': 's',
            'zht': 't',
            'zhtw': 'tw',
            'zhhk': 'hk',
            'zhcn': 's',
            '_': '',
        }

        for k, v in mappings.items():
            config_name = config_name.replace(k, v)

        return config_name

    @property
    def executable(self):
        return self._executable

    @property
    def configs(self):
        """Get supported config names

        :return: A list of config names
        :rtype: str
        """

        if not self._cfgs:
            # Search new style config file names
            cfgs = dict()

            is_old_style_config = False
            file_paths = glob.glob(os.path.join(self._cfg_dir, '*.json'))
            if not file_paths:
                # Search old style config file names
                file_paths = glob.glob(os.path.join(self._cfg_dir, '*.ini'))
                is_old_style_config = True

            for apath in file_paths:
                base_name = os.path.basename(apath)
                key = os.path.splitext(base_name)[0]
                if is_old_style_config:
                    key = self._config_to_new_style(key)

                cfgs[key] = base_name

            self._cfgs = cfgs

        return self._cfgs.keys()
