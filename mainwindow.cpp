#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)

{

    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}
void MainWindow::on_lineEdit_returnPressed()
{
    QString input = ui->lineEdit->text();
    ui->lineEdit_2->setText(input);
}


void MainWindow::on_pushButton_clicked()
{
    QString input = ui->lineEdit->text();
    ui->lineEdit_2->setText(input + ": ");
}

void MainWindow::on_reset_clicked()
{
    ui->lineEdit->setText("");
}



void MainWindow::on_pushButton_5_clicked()
{
    QString threshLow = ui->lineEdit_7->text();
     QString threshHigh = ui->lineEdit_8->text();
}
void MainWindow::on_reset_5_clicked()
{
   ui->lineEdit_7->setText("");
     ui->lineEdit_8->setText("");
}

void MainWindow::on_lineEdit_4_returnPressed()
{
    QString keyRow = ui->lineEdit_4->text();

}
void MainWindow::on_lineEdit_3_returnPressed()
{
    QString column = ui->lineEdit_3->text();

}


void MainWindow::on_lineEdit_9_returnPressed()
{
    QString keyColumn = ui->lineEdit_9->text();
}

void MainWindow::on_pushButton_4_clicked()
{
    QString colPlotx = ui->lineEdit_5->text();
    QString colPloty = ui->lineEdit_6->text();
}

void MainWindow::on_reset_4_clicked()
{
     ui->lineEdit_5->setText("");
     ui->lineEdit_6->setText("");
}

void MainWindow::on_reset_6_clicked()
{
    ui->lineEdit_9->setText("");
}

void MainWindow::on_reset_3_clicked()
{
    ui->lineEdit_4->setText("");
}

void MainWindow::on_pushButton_3_clicked()
{
    QString keyRow = ui->lineEdit_4->text();
}

void MainWindow::on_pushButton_2_clicked()
{
    QString column = ui->lineEdit_3->text();
}

void MainWindow::on_reset_2_clicked()
{
    ui->lineEdit_3->setText("");
}
