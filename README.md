# rqt templates

A collection of templates to generate ROS2 packages defining new rqt plugins.
A new package can be created using the [template2instance](https://github.com/yguel/template2instance) python tool

``` bash
poetry run create template_folder new_package_name
```

In the ui folder a ui file should be created using the qt designer tool.
The ui file should contain a MainWindow widget named MyPackageMainWindow
where MyPackage is the name of the package in camel case.
If you are unsure how to name your MainWindow widget have a look at the file ``include/rqt_plugin.hpp``, the ``ui_`` object type name is the name of the MainWindow widget.

Look at the lines below to see how the MainWindow widget is declared in the ``include/rqt_plugin.hpp`` file:
```cpp
class MyPackagePlugin : public rqt_gui_cpp::Plugin
{
  Q_OBJECT

  ...

private:
  Ui::MyPackageMainWindow ui_;

  ...
};
```
In the qt designer tool you can set the name of the MainWindow widget by clicking on the QMainWindow widget in the Object Inspector, in the right panel and either:
* set the objectName property of the QObject to MyPackageMainWindow in the Property Editor panel below the Object Inspector or
* double clicking on the object name in the Object Inspector and changing the name in the input box that will appear in place of the object name.
