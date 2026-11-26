#include <iostream>
#include <cv>

int main(){
    cv::Mat immagine = cv::imread("input.jpg", cv::IMREAD_COLOR);
    if(immagine.empty()){
        std::cerr << "Errore: impossibile leggere l'immagine." << std::endl;
    }

    if(!immagine.isContinuos()){
        immagine = immagine.clone();
    }

    unsigned int numPixel = static_cast<unsigned int>(immagine.rows * immagine.cols);

    cv::Mat immagineBinaria(immagine.rows,immagine.cols,CV_8UC1);
    binarizeImage();

    if(!cv:imwrite("output_bw.ong",immagineBinaria)){
        std::cerr << "Errore: Impossibile salvare l'immagine" << std::endl;
    }

    std::cout << "Immagine salvata" << std::endl;
    return 0;
}