#########################################################
Place holder variables for substitution in the templates
#########################################################

******************
List of Variables
******************

1. PACKAGE_NAME : Name of the package (e.g. rqt_profilobot)
2. PACKAGE_VERSION : Version of the package in semantic versioning (e.g. 0.0.1)
3. PACKAGE_DESCRIPTION : Description of the package, a free text (e.g. A simple rqt plugin for controlling and monitoring the Profilobot)
4. PACKAGE_MAINTAINER_EMAIL : Email of the maintainer (e.g. maintainer@gmail.com)
5. PACKAGE_MAINTAINER_NAME : Full name of the maintainer, first name in lower case, capitalized and last name in upper case (e.g. Manuel YGUEL)
6. PACKAGE_LICENSE : License of the package, ideally one of ["Apache-2.0","BSL-1.0","BSD-2.0","BSD-2-Clause","BSD-3-Clause","GPL-3.0-only","LGPL-3.0-only","MIT","MIT-0"]
7. CAMEL_CASE_PACKAGE_NAME : Name of the package in camel case (e.g. RqtProfilobot)
8. UNCAPITALIZED_CAMEL_CASE_PACKAGE_NAME : Name of the package in camel case without the first letter capitalized (e.g. rqtProfilobot)
9.  OBJECT_HUMAN_NAME : Human readable name of the object, in title case (e.g. RQT Profilobot UI)
10. YEAR : Year of the creation
11. LABORATORY : Name of the laboratory for copyright declaration
12. LICENSE_TEXT : Text of the license, corresponding to one of the texts of ["Apache-2.0","BSL-1.0","BSD-2.0","BSD-2-Clause","BSD-3-Clause","GPL-3.0-only","LGPL-3.0-only","MIT","MIT-0"]
13. UPPER_CASE_PACKAGE_NAME : Name of the package in upper case (e.g. RQT_PROFIOBOT)
14. LABEL_GROUP : Label of the plugin in the rqt_gui (default: _Robot Control_)
15. ICON_GROUP : Icon of the plugin in the rqt_gui (default: folder)
16. STATUS_TIP_GROUP : Status tip of the plugin in the rqt_gui (default: Plugins related to the robot control related to OBJECT_HUMAN_NAME.)
17. LABEL : (default: OBJECT_HUMAN_NAME)
18. ICON : (default: image-x-generic)
19. STATUS_TIP : (default: An REPLACE_UNDERSCORE_WITH_SPACE(PACKAGE_NAME) control planel.)

************************
Naming of UI components
************************

1. The MainWindow should be named as follows: %(CAMEL_CASE_PACKAGE_NAME)sMainWindow (e.g. RqtProfilobotMainWindow)
2. The header corresponding to the ui file should be named as follows: ui_%(UNCAPITALIZED_CAMEL_CASE_PACKAGE_NAME)s.h (e.g. ui_rqtProfilobot.h)
3. The ui file should be named as follows: %(UNCAPITALIZED_CAMEL_CASE_PACKAGE_NAME)s.ui (e.g. rqtProfilobot.ui) and placed in the ui folder.