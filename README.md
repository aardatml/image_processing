# Trafik Levhası Tespiti (OpenCV)

Bu proje, verilen bir görüntüdeki trafik levhasını **renk ve şekil bilgisine göre** tespit eder.  
Levhanın **türünü** (uyarı, yasak, zorunlu) ve **yaklaşık mesafesini** belirler.

## Kullanılan Teknolojiler
- Python
- OpenCV
- NumPy
- Matplotlib

## Çalışma Mantığı
- Görüntü HSV renk uzayına çevrilir.
- Kırmızı ve mavi renkler maskeleme ile ayrılır.
- Kenar ve kontur analizi yapılır.
- Şekle göre levha türü belirlenir:
  - Üçgen → Uyarı Levhası  
  - Daire → Yasak / Zorunlu Levha (renge göre)
- Levhanın görüntüde kapladığı alana göre mesafe tahmini yapılır.

