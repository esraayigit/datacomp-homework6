# datacomp-homework6
# Arithmetic Coding Simulation
 Bu proje, basit bir aritmetik kodlama (arithmetic coding) simülasyonunu içerir. Aşağıdaki adımlarla PMF (Probability Mass Function) başlatılır ve giriş akışındaki her sembol işlendiğinde güncellenir:

initialize_pmf(num_symbols, V): Verilen sembol sayısına ve V bitlik bir doğruluk düzeyine göre PMF başlatılır. Bu fonksiyon başlangıç olasılıklarını dengeli bir şekilde dağıtır ve toplamı 2^V olacak şekilde ayarlamalar yapar.

update_pmf(pmf, symbol, V, increment): PMF'yi belirtilen sembole göre günceller. Yeni toplam 2^V'yi aşarsa, ölçeklendirme uygulanır ve tüm olasılıklar en az 1 olacak şekilde düzeltilir. Eğer toplam düşük kalırsa, eksik değer eşit şekilde dağıtılır.

arithmetic_coding(pmf, symbol): Güncel PMF ve sembole göre kodlama işlemine başlar. (Kodlama detayları ileride eklenecektir.)

# Kod Özellikleri:
- PMF Yönetimi: Dinamik olarak sembol istatistiklerini güncelleyerek aritmetik kodlamanın temelini sağlar.
- Esneklik: V değeri ve sembol sayısı parametrelerle kontrol edilebilir.
- Geliştirilmeye Uygun: Kodlama fonksiyonu genişletilmeye açıktır.
# Kullanım:
initialize_pmf fonksiyonu ile başlangıç PMF'sini oluşturun.
Giriş sembollerini update_pmf ve arithmetic_coding ile sırayla işleyin.
Her güncellemede PMF'nin nasıl değiştiğini gözlemleyin.
Bu proje, aritmetik kodlama algoritmalarını öğrenmek veya temel simülasyonlar yapmak isteyenler için örnek bir başlangıç noktasıdır.
