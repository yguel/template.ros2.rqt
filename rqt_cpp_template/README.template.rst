#################################
%(PACKAGE_NAME)s ROS2 package
#################################

%(PACKAGE_DESCRIPTION)s

****
Run 
****

================
Standalone mode
================

How to run the %(PACKAGE_NAME)s gui.

.. code-block:: bash

   rqt --force-discover --standalone %(PACKAGE_NAME)s

or 

.. code-block:: bash

   rqt --force-discover -s %(PACKAGE_NAME)s


================
As a RQT plugin
================

Launch the rqt GUI

.. code-block:: bash

   rqt --clear-config --force-discover

Then add the plugin from the menu: Plugins -> %(PACKAGE_CATEGORY)s -> %(PACKAGE_NAME)s