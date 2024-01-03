<template>
  <v-card>
    <v-row>
      <v-col cols="4" style="margin-left: 50px; margin-top: 30px;">
        <v-btn @click="show()"> Start classifier </v-btn>
      </v-col>
    </v-row>
        <v-card-text v-show="showAcc">
      <v-card-title>Summarize:</v-card-title>
      <p style="margin-left: 70px;">
        <p>Accuracy : {{ listAcc[0] }}</p>
        <p>F1-score : {{ listAcc[1] }}</p>
        <p>Recall : {{ listAcc[2] }}</p>
        <p>Precision : {{ listAcc[3] }}</p>
        <p>
          Số lượng dữ liệu dự đoán đúng : {{ listAcc[4] }} /
          {{ listAcc[4] + listAcc[5] }}
        </p>
        <p>
          Số lượng dữ liệu dự đoán sai : {{ listAcc[5] }} /
          {{ listAcc[4] + listAcc[5] }}
        </p>
      </p>
    </v-card-text>
    <v-row v-show="showResult">
      <v-col cols="3" v-for="item in list" :key="item.index">
        <img
          :src="'data:image/jpeg;base64,' + item.image"
          style="
            filter: invert(100%);
            width: 300px;
            height: 300px;
            margin-left: 50px;
            border: 1px solid black;
          "
        />
        <p style="margin-left: 50px; color: blue">
          Nhãn dự đoán: {{ item.predicted_label }}
        </p>
        <p style="margin-left: 50px; color: red">
          Nhãn thực tế: {{ item.true_label }}
        </p>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import doAnApi from "@/doAn";
export default {
  data() {
    return {
      list: [],
      listAcc: [],
      showResult: false,
      showAcc: false,
      x: "01",
      imageList: [{ x: "01" }],
      i: 0,
      k: 0,
    };
  },
  methods: {
    async getAll() {
      this.list = await doAnApi.getAll();
      return this.list;
    },
    async getAcc() {
      this.listAcc = await doAnApi.getResults();
      return this.listAcc;
    },
    show() {
      this.showResult = !this.showResult;
      this.showAcc = !this.showAcc;
    },
  },
  created() {
    this.getAll();
    this.getAcc();
  },
};
</script>

<style></style>
