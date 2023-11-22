# book_api
This Book API project

[!NOTE]
Loyiha demo holatda

[![GitHub top language](https://img.shields.io/github/languages/top/okh-engineer/book_api?style=flat-square&logo=github)](https://github.com/okh-engineer/book_api)

Ushbu loyiha telegramdagi kitob tarqatuvchi kanal va guruhlardagi kitoblarni bir joyga jamlash, ularni oson saralash uchun yaratildi. 

## Foydalanilgan kanal/guruhlar
<details>
<summary>Loyihadagi kitob fayllarini olishda quyidagi telegram kanallardan foydalanildi</summary>
<ol>

  <li>TKTI_library</li>
  <li>kitobN11</li>
  <li>KITOBLAR_BAZASI</li>
  <li>audio_kitobxona</li>
  <li> Elektron_pdf_islomiy_kitoblar_ap</li>
  <li> kutubxona_kitoblar_audio_elektro</li>
  <li> kitoblar_baza</li>
  <li>kitoblar_bazam</li>
  <li>kitoblar_bazasi</li>
  <li>KITOBLAR_BAZASl</li>
  <li>URGUT_KUTUBXONA_KITOBLAR_BAZASI</li>
  <li>Audio_Kutubxona_uz</li>
  <li>audio_Apk_kutubxona_pdf_kitoblar</li>
  <li>e_kutubxona</li>
  <li>audiokitob_eshitamiz</li>
  <li>kutubxona7</li>
  <li>KitoblarBazas</li>
va barcha fayllar ostiga kanal manzili biriktirildi.
</ol>
</details>


## Loyiha haqida

Loyiha 83 ming dan ortiq kitob, maqola, testlar to'plamlarining fayllarini va 17 mingdan ortiq audio formatdagi kitoblarni o'z ichiga oladi.

Loyihani yaratishda mualliflik huquqlarini e'tiborga olishga harakat qilindi. Loyiha 83 mingdan ziyod fayldan tashkil topganini hisobga olib bazi kitoblar o'tkazib yuborilgan bo'lishi mumkin.
Iltimos bu haqida menga xabar bering

> Bu loyiha hozir sinov bosqichidan o'tmoqda. Agarda biror xatolikka duchor
> bo'lsangiz, xatolik haqida [xabardor](https://github.com/okh-engineer/book_api/issues/new)
> qilishni unutmang.

Loyihani demo holatda https://mlibrary.up.railway.app/api/file-book-api/?search=query ushbu manzilga query o'rniga kitob nomini kiritish orqali ishlatib ko'rish mumkin. Loyiha bepul serverda joylashganligi va resurslar cheklanganligi uchun loyihadan foydalanish kunlik 10 ta so'rov bilan cheklangan.

## Loyihani ishlab chiqishda uchralgan qiyinchiliklar va yechimlari STAR metodi orqali
<details>
  <summary>
    1-muammo. Ma'lumotlarni jamlash va saralash
  </summary>
  <br>
  <ul>
      <li>
        Telegramdagi bir qancha kitob tarqatuvchi kanal va guruhlar bor va ulardagi kitob ma'lumotlarini yaratilgan model asosida ma'lumotlar omboriga qo'shish kerak. Albatta kitoblar fayllari 80 mingdan ko'p ekanligini hisobga olganda buni manual holatda bajarish imkonsiz
      </li>
      <li>
        Bu ma'lumotlarni python orqali yig'ib, uni kod orqali ma'lumotlar bazasiga qo'shmoqchi bo'ldim
      </li>
      <li>
        Buning uchun internetda mavjud bo'lgan resurslardan foydalanish uchun izlanish o'tkardim va bir nechta yechimlar ichidan https://github.com/estebanpdl/telegram-tracker bu repositoryda joylashgan koddan foydalanishga qaror qildim, sababi uchbu kod orqali bir nechta kanaldagi ma'lumotlarni bitta faylda to'plash mumkin edi. Bu esa kod orqali fayllarni boshqarishni osonlashtirdi
        Barcha ma'lumotlarni bitta faylda yig'ildani yaxshi lekin bu fayl hajmi githubning fayl limitidan oshib ketdi, men fayllarni ma'lumotlar bazasiga qo'shish uchun online serverdan foydalanmoqchiligim uchun u fayl github repo sida bo'lishi kerak edi. Men nega fayl hajmi bunchalik katta bo'lganligini sabablarini qidirdim. Fayl hajmi katta ekanligiga sabab yuqoridagi data scraper telegram kanaldagi barcha xabarlar ma'lumotlarini olib faylga joylagani edi ya'ni mening faylimda kanalga yuborilgan text, audio, reklama, sticker va shunga o'xshash xabarlarning barchasi mavjud edi. Men bu fayldagi ma'lumotlarni saralashim va fayl turiga qarab alohida faylga joylashim kerak edi. Buning uchun Pandas kutubxonasidan foydalandim, bunu ishlatishda internetdagi ma'lumotlar va ChatGPT katta yordam berdi.  
      </li>
      <li>
      Saralash yakunlangandan so'ng endi menda limitni oshmagan va faqatgina kerakli ma'lumotlardan tashkil topgan fayl bor edi. Buning natijasida online serverda ma'lumotlarni qo'shishim mumkin edi
      </li>
    </ul>
</details>

<details>  
  <summary>
    2-muammo. Fayllarni yagona telegram kanalda to'plash va ularning nomlarini lotin alifbosiga o'tkazish
  </summary>
    <br>
    <ul>
      <li>
        Loyihada kitob nomlari kirill va lotin alifbosida yozilgan edi va bu ma'lumotlar omboridan kitoblarni saralashda qiyinchilik tug'dirdi va kitob fayllari ko'plab kanallarda joylashganligi ularni yo'qolib qolish havfini oshirdi.
      </li>
      <li>
        Loyihadagi fayllarni saralash oson bo'lishi uchun fayllar ismini lotin alifbosiga o'tkazishim va fayllarni barchasini yagona telegram kanalda to'plashim kerak edi.
      </li>
      <li>
        Ma'lumotlar bazasiga model asosida kitob ma'lumotlarini kiritishdan oldin kitob nomlari kiril alifbosida ekanligi yoki emasligini tekshirishim kerak edi. Buning uchun internetdan yozuv alifbosini aniqlash uchun sodda funksiya topdim va uni ishlatib ko'rdim, hammasi joyida funksiya ishladi. Endi aniqlangan kirill alifbosidagi kitob nomlarini lotin alifbosiga o'tkazishim kerak edi. Buning uchun avvalroq eshitganim <a href="https://korrektor.uz/">korrektor.uz</a> loyihasidan foydalandim, to'g'risi loyiha asosida python kutubxonasi ishlab chiqilgani va korrektor.uz dan foydalanish Uzinfocom tufayli bepul bo'lgani menga juda qo'l keldi. Barcha fayl nomlari lotin alifbosida ma'lumotlar bazasiga joylanganidan so'ng bu ma'lumotlar asosida barcha fayllarni yagona telegram kanalda to'plash uchun telegram bot kodladim va uni ishga tushirdim.
      </li>
      <li>
        Bu ishlarning tufayli endi loyihadagi barcha fayl nomlari lotin alifbosida saqlangan va ularni saralash osonlashgan edi. Yana fayllar yo'qolib qolmasligi uchun barcha fayllar yagona telegram kanalda muvaffiqiyatli joylandi.
      </li>
    </ul>
</details>

Loyihani telegram orqali ham https://t.me/mobilkutubxona_bot ushbu bot orqali ishlatib ko'rishingiz mumkin. Xatoliklar haqida iltimos xabar bering.

Rahmat

