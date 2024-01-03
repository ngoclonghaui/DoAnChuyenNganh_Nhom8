import axiosClient from "./axiosClient";
const doAnApi = {
  getAll: (params = null) => {
    const url = "api/getall";
    return axiosClient.get(url, params);
  },
  getResults: (params = null) => {
    const url = "results";
    return axiosClient.get(url, params);
  },
};
export default doAnApi;
