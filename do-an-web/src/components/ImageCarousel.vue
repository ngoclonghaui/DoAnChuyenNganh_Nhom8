<template>
  <v-row
    style="
      background: linear-gradient(45deg, #d8bfd8, #ffffe0);
      margin-top: -0px;
    "
  >
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Affenhuahua Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listImage" :key="item.id">
          <v-img :src="item" style="width: 400px; height: 400px"></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Afgan Hound Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listImageAfgan" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Akita Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listImageAkita" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="
              width: 400px;
              height: 400px;
              justify-content: center;
              align-items: center;
            "
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
  </v-row>
  <v-row
    style="background: linear-gradient(45deg, #d8bfd8, #ffffe0); margin-top: -0"
  >
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Alaskan Malamute Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listImageAlaskan" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> American Bulldog Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listImageAmerican" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Auggie Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listAuggie" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="
              width: 400px;
              height: 400px;
              justify-content: center;
              align-items: center;
            "
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
  </v-row>
  <v-row
    style="background: linear-gradient(45deg, #d8bfd8, #ffffe0); margin-top: -0"
  >
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog">Beagle Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listBeagle" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Belgian Tervuren Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listBelgian" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Bichon Frise Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listBichon" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="
              width: 400px;
              height: 400px;
              justify-content: center;
              align-items: center;
            "
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
  </v-row>
  <v-row
    style="background: linear-gradient(45deg, #d8bfd8, #ffffe0); margin-top: -0"
  >
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog">Bocker Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listBocker" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog">Borzoi Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listBorzoi" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Boxer Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listBoxer" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="
              width: 400px;
              height: 400px;
              justify-content: center;
              align-items: center;
            "
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
  </v-row>
  <v-row
    style="background: linear-gradient(45deg, #d8bfd8, #ffffe0); margin-top: -0"
  >
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog">Bugg Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listBugg" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4" class="col_style">
      <v-card-text class="name_dog"> Bulldog Dog </v-card-text>
      <v-carousel
        cycle
        hide-delimiters
        show-arrows="hover"
        :interval="3000"
        style="height: 400px; width: 400px"
      >
        <v-carousel-item v-for="item in listBull" :key="item.id">
          <v-img
            :src="item + '.jpg'"
            style="width: 400px; height: 400px"
          ></v-img>
        </v-carousel-item>
      </v-carousel>
    </v-col>
    <v-col cols="4">
      
    </v-col>
  </v-row>
</template>

<script>
import Image1 from "../test/Affenhuahua dog/Image_1.jpg";
import Image2 from "../test/Affenhuahua dog/Image_2.jpg";
import Image16 from "../test/Affenhuahua dog/Image_16.jpg";
import Image20 from "../test/Affenhuahua dog/Image_20.jpg";
import Image48 from "../test/Affenhuahua dog/Image_48.jpg";

export default {
  data() {
    return {
      listImage: [Image1, Image2, Image16, Image20, Image48],
      listImageAfgan: [],
      listImageAkita: [],
      listImageAlaskan: [],
      listImageAmerican: [],
      listAuggie: [],
      listBeagle: [],
      listBelgian: [],
      listBichon: [],
      listBocker: [],
      listBorzoi: [],
      listBoxer: [],
      listBugg: [],
      listBull: [],
      index: 1,
      pathAfgan: "../src/test/Afgan Hound dog/",
      pathAkita: "../src/test/Akita dog/",
      pathAlaskan: "../src/test/Alaskan Malamute dog/",
      pathAmerican: "../src/test/American Bulldog dog/",
      pathAugie: "../src/test/Auggie dog/",
      pathBeagle: "../src/test/Beagle dog/",
      pathBelgian: "../src/test/Belgian Tervuren dog/",
      pathBichon: "../src/test/Bichon Frise dog/",
      pathBocker: "../src/test/Bocker dog/",
      pathBorzoi: "../src/test/Borzoi dog/",
      pathBoxer: "../src/test/Boxer dog/",
      pathBugg: "../src/test/Bugg dog/",
      pathBull: "../src/test/Bulldog dog/",
    };
  },
  methods: {
    getAfganDogPath() {
      while (this.index <= 10) {
        this.listImageAfgan.push(this.pathAfgan + "Image_" + this.index);
        this.index++;
      }
    },
    getAkitaDogPath() {
      this.index = 1;
      while (this.index <= 11) {
        this.listImageAkita.push(this.pathAkita + "Image_" + this.index);
        this.index++;
      }
    },
    getAlaskanDogPath() {
      this.index = 1;
      while (this.index <= 10) {
        this.listImageAlaskan.push(this.pathAlaskan + "Image_" + this.index);
        this.index++;
      }
    },
    getAmericanDogPath() {
      this.index = 1;
      while (this.index <= 10) {
        this.listImageAmerican.push(this.pathAmerican + "Image_" + this.index);
        this.index++;
      }
    },
    getAuggieDogPath() {
      this.index = 1;
      while (this.index <= 8) {
        this.listAuggie.push(this.pathAugie + "Image_" + this.index);
        this.index++;
      }
    },
    getBeagleDogPath() {
      this.index = 1;
      while (this.index <= 5) {
        this.listBeagle.push(this.pathBeagle + "Image_" + this.index);
        this.index++;
      }
    },
    getBelgianDogPath() {
      this.index = 1;
      while (this.index <= 10) {
        this.listBelgian.push(this.pathBelgian + "Image_" + this.index);
        this.index++;
      }
    },
    getBichonDogPath() {
      this.index = 1;
      while (this.index <= 10) {
        this.listBichon.push(this.pathBichon + "Image_" + this.index);
        this.index++;
      }
    },
    getBockerDogPath() {
      this.index = 1;
      while (this.index <= 6) {
        this.listBocker.push(this.pathBocker + "Image_" + this.index);
        this.index++;
      }
    },
    getBorzoiDogPath() {
      this.index = 1;
      while (this.index <= 10) {
        this.listBorzoi.push(this.pathBorzoi + "Image_" + this.index);
        this.index++;
      }
    },
    getBoxerDogPath() {
      this.index = 1;
      while (this.index <= 5) {
        this.listBoxer.push(this.pathBoxer + "Image_" + this.index);
        this.index++;
      }
    },
    getBuggDogPath() {
      this.index = 1;
      while (this.index <= 10) {
        this.listBugg.push(this.pathBugg + "Image_" + this.index);
        this.index++;
      }
    },
    getBullDogPath() {
      this.index = 1;
      while (this.index <= 6) {
        this.listBull.push(this.pathBull + "Image_" + this.index);
        this.index++;
      }
    },
  },
  created() {
    this.getAfganDogPath();
    this.getAkitaDogPath();
    this.getAlaskanDogPath();
    this.getAmericanDogPath();
    this.getAuggieDogPath();
    this.getBeagleDogPath();
    this.getBelgianDogPath();
    this.getBichonDogPath();
    this.getBockerDogPath();
    this.getBorzoiDogPath();
    this.getBoxerDogPath();
    this.getBuggDogPath();
    this.getBullDogPath();
  },
};
</script>

<style scoped>
.col_style {
  border: 1px solid black;
}
.name_dog {
  margin: auto;
  font-size: 20px;
  color: rgb(78, 78, 197);
  font-family: sans-serif;
  margin-left: 50px;
}
</style>