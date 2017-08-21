#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_lineEdit_returnPressed();


    void on_pushButton_clicked();

    void on_reset_clicked();



    void on_pushButton_5_clicked();


    void on_lineEdit_4_returnPressed();

    void on_lineEdit_3_returnPressed();

    void on_lineEdit_9_returnPressed();

    void on_pushButton_4_clicked();


    void on_reset_5_clicked();

    void on_reset_4_clicked();

    void on_reset_6_clicked();

    void on_reset_3_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_2_clicked();

    void on_reset_2_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
