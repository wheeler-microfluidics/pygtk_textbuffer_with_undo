from distutils.core import setup

import version


setup(name='pygtk-textbuffer-with-undo',
      version=version.getVersion(),
      description='GTK textbuffer with undo functionality.',
      keywords='gtk undo buffer text input widget',
      author='Florian Heinle and Christian Fobel',
      author_email='christian at fobel dot net',
      url='http://github.com/cfobel/pygtk_textbuffer_with_undo.git',
      license='GPL',
      packages=['textbuffer_with_undo'])
