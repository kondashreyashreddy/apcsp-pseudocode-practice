netflix_basic_price <- 10.99
netflix_premium_price <- 21.99

crunchyroll_basic_price <- 9.99
crunchyroll_pro_price <- 10.99
crunchyroll_elite_price <- 11.99

ap_exam <- 110.00
prime_video <- 1.24

netflix_difference <- netflix_premium_price - netflix_basic_price

crunchyroll_difference_elite_pro <- crunchyroll_elite_price - crunchyroll_pro_price
crunchyroll_difference_pro_basic <- crunchyroll_pro_price - crunchyroll_basic_price
crunchyroll_avg_difference <- (crunchyroll_difference_elite_pro + crunchyroll_difference_pro_basic) / 2

ap_prime_difference <- ap_exam - prime_video

DISPLAY("The difference between netflix premium & netflix basic is " + netflix_difference + ", ")
DISPLAY("the difference between crunchyroll elite & crunchyroll pro is " + crunchyroll_elite_pro + ", ")
DISPLAY("the difference between crunchyroll pro & crunchyroll basic is " + crunchyroll_pro_basic + ", ")
DISPLAY("the average difference between crunchyroll plans is " + crunchyroll_avg_difference + ", ")
DISPLAY"and the difference between ap exams & prime video is " + ap_prime_difference + ".")
