const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const userSchema = new Schema({
    adsoyad: String,
    yas: Number,
    telefon: String,
    email: String,
    createdAt: String,
    updatedAt: String,
});

const Users = mongoose.model("Users", userSchema);
module.exports = Users;

//----------------------------------------------------------------------------------------------------------------

const dbURL = "mongodb+srv://";
mongoose.connect(dbURL, { useUnifiedTopology: true, useNewUrlParser: true, useFindAndModify: false, })
    .then((result) => console.log("Baglanti kuruldu"))
    .catch((err) => console.log(err));

//----------------------------------------------------------------------------------------------------------------

// Yeni kayıt ekleme.
const User = new Users();
User.adsoyad = "enes";
User.telefon = "096565131321";
User.yas = 20
User.email = "enes@example.com";
User.createdAt = new Date().toLocaleString();
User.save().then((result) => {
    console.log(result);
});

//----------------------------------------------------------------------------------------------------------------

// Tüm kayıtları listeler.
Users.find().then((result) => {
    console.log(result);
});

// Koşullu listeleme. (and)
Users.find({ adsoyad: "enes", yas: 20 }).then((result) => {
    console.log(result);
});

// Belirtilen id değerine ait kaydı getirir.
Users.findById("611ea773788a013b2029aba4").then((result) => {
    console.log(result);
});

// İlk bulduğu kaydı getirir.
Users.findOne({ adsoyad: "enes" }).then((result) => {
    console.log(result);
});

// Yaşı, belirtilen değerden küçük olanları listeler.
Users.find({ yas: { $lt: 30 } }).then((result) => {
    console.log(result);
});

// Yaşı belirtilen değere eşit veya büyük olanları listler.
Users.find({ yas: { $gte: 40 } }).then((result) => {
    console.log(result);
});

// Tüm kayıtları adsoyad'a göre alfabetik olarak listeler.
Users.find().sort({ adsoyad: 1 }).then((result) => {
    console.log(result);
});

// Tüm kayıtları adsoyad'a göre alfabenin tersine göre listeler.
Users.find().sort({ adsoyad: -1 }).then((result) => {
    console.log(result);
});

// adsoyadı s harfi ile başlayanları listeler.
Users.find({ adsoyad: { $regex: "^s" } }).then((result) => {
    console.log(result);
});

// Belirtilen sayıda kayıt listeler.
Users.find().limit(2).then((result) => {
    console.log(result);
});

//----------------------------------------------------------------------------------------------------------------

// Belirtilen id'deki kaydı değiştirir. (mevcut/değişecek)
Users.findByIdAndUpdate("611ea773788a013b2029aba4", { adsoyad: "enes" }).then(
    (result) => { }
);

// Belirtilen değerdeki kaydı, yeni verilen değer ile değiştirir. (mevcut/değişecek)
Users.findOneAndUpdate({ adsoyad: "enes" }, { adsoyad: "james" }).then(
    (result) => { }
);

//----------------------------------------------------------------------------------------------------------------

// Belirtilen id değerine ait kaydı siler.
Users.findByIdAndDelete("611ea773788a013b2029aba4").then((result) => { });

// Belirtilen değere ait kaydı siler.
Users.findOneAndDelete({ adsoyad: "enes" }).then((result) => { });

// Cluster'daki tüm kayıtları siler.
Users.deleteMany().then((result) => { });

//----------------------------------------------------------------------------------------------------------------


/*
.then((result)=>{
        console.log(result)
    })
.catch((err)=>{
    console.log(err)
})
*/
