#inlcude <iostream>

int main(){
    cv::Mat immagine = cv::imread("input.jpg", cv::IMREAD_COLOR);
    if(immagine.empty()){
        std::cerr << "Errore: impossibile leggere l'immagine." << std::endl
    }

}