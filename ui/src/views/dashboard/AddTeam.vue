<template>
  <div class="card">
    <h1 class="title">Available Riders</h1>
  </div>
  <div class="container">
    <div class="d-flex">
      <div class="col-lg-3" v-for="(rider, index) in riders" :key="rider">
        <!-- Main content -->
        <div class="row">
          <div class="col-lg-12">
            <!-- Payment -->
            <div class="card mb-4">
              <div class="card-body">
                <!-- Title -->
                <div class="justify-content-between align-items-center py-3">
                  <h2 class="h5 mb-0">
                    <a href="#" class="text-muted"></a>{{ rider.bike_model }}
                  </h2>
                </div>
                <!-- Image -->
                <div
                  class="justify-content-center align-items-center py-3 m-auto"
                >
                  <img
                    :src="rider.bike_img"
                    class="m-auto"
                    height="100"
                    width="120"
                  />
                </div>
                <div class="row">
                  <div class="col-lg-12">
                    <h3 class="h6">Payment Info</h3>
                    <p>
                      Starting Cost: KShs. 10
                      <span class="badge bg-success rounded-pill"
                        >POST PAY</span
                      >
                    </p>
                    <p>
                      <span class="d-inline">Payment Methods&nbsp;</span>
                      <span class="d-inline badge bg-success rounded-pill"
                        >MPesa</span
                      >
                      <span class="d-inline badge bg-success rounded-pill"
                        >Cash</span
                      >
                    </p>
                  </div>
                  <div class="col-lg-12">
                    <h3 class="h6">Rider Info</h3>
                    <address>
                      <strong
                        >Name:{{ users[index].first_name }}
                        {{ users[index].last_name }}</strong
                      ><br />Address: {{ rider.address }},{{ rider.city }}<br />
                      <span title="Phone">TEL:</span> {{ users[index].tel }}
                    </address>
                  </div>
                  <div class="rate bg-success py-3 text-white mt-3 m-auto">
                    <h6 class="mb-0">Rating</h6>

                    <div class="rating">
                      <input
                        type="radio"
                        name="rating"
                        value="5"
                        id="5"
                      /><label for="5">☆</label>
                      <input
                        type="radio"
                        name="rating"
                        value="4"
                        id="4"
                      /><label for="4">☆</label>
                      <input
                        type="radio"
                        name="rating"
                        value="3"
                        id="3"
                      /><label for="3">☆</label>
                      <input
                        type="radio"
                        name="rating"
                        value="2"
                        id="2"
                      /><label for="2">☆</label>
                      <input
                        type="radio"
                        name="rating"
                        value="1"
                        id="1"
                      /><label for="1">☆</label>
                    </div>

                    <div class="buttons px-4 mt-0 col-lg-12">
                      <form @submit.prevent="placeRide(rider.id)">
                        <button
                          type="submit"
                          class="btn btn-warning btn-block rating-submit"
                        >
                          Confirm Driver
                        </button>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <p></p>
</template>

<script>
import axios from "axios";

import { toast } from "bulma-toast";

export default {
  name: "Riders",
  data() {
    return {
      name: "",
      tel: "",
      riders: [],
      users: [],
      rider: "",
      client: "",
      source: localStorage.getItem("from"),
      dest: localStorage.getItem("dest"),
    };
  },
  mounted() {
    this.updatearray();
    console.log(localStorage.getItem("from"));
    console.log(localStorage.getItem("dest"));
  },
  methods: {
    async updatearray() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("riders/")
        .then((response) => {
          console.log(response);
          this.riders = response.data;
          toast({
            message: "Available Rides loaded!",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "top-right",
          });
          for (var i = 0; i < this.riders.length; i++) {
            //console.log(this.riders[i].id);
            axios.get("listusers/" + response.data[i].user).then((res) => {
              //console.log(res.data);
              this.users.push({
                username: res.data.username,
                first_name: res.data.first_name,
                last_name: res.data.last_name,
                tel: res.data.tel,
              });
            });
          }
          for (var i = 0; i < this.users.length; i++) {
            console.log(this.users[i]);
          }
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    async placeRide(rider, tel) {
      this.$store.commit("setIsLoading", true);
      const data = {
        rider: rider,
        client: localStorage.getItem("userid"),
        sorce: this.source,
        destination: this.dest,
      };
      await axios
        .post("rides/", data)
        .then((response) => {
          console.log(response);
          this.riders = response.data;
          toast({
            message:
              "Your ride has been placed!\nPlease check for details in your account!",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 5000,
            position: "top-center",
          });
          localStorage.removeItem("from");
          localStorage.removeItem("dest");
          this.$router.push({ name: "MyAccount" });
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
<style scoped>
body {
  background-color: #f7f6f6;
}

.card {
  width: 350px;
  border: none;
  box-shadow: 5px 6px 6px 2px #e9ecef;
  border-radius: 12px;
}

.circle-image img {
  border: 6px solid #fff;
  border-radius: 100%;
  padding: 0px;
  top: -28px;
  position: relative;
  width: 70px;
  height: 70px;
  border-radius: 100%;
  z-index: 1;
  background: #e7d184;
  cursor: pointer;
}

.dot {
  height: 18px;
  width: 18px;
  background-color: blue;
  border-radius: 50%;
  display: inline-block;
  position: relative;
  border: 3px solid #fff;
  top: -48px;
  left: 186px;
  z-index: 1000;
}

.name {
  margin-top: -21px;
  font-size: 18px;
}

.fw-500 {
  font-weight: 500 !important;
}

.start {
  color: green;
}

.stop {
  color: red;
}

.rate {
  border-bottom-right-radius: 12px;
  border-bottom-left-radius: 12px;
}

.rating {
  display: flex;
  flex-direction: row-reverse;
  justify-content: center;
}

.rating > input {
  display: none;
}

.rating > label {
  position: relative;
  width: 1em;
  font-size: 30px;
  font-weight: 300;
  color: #ffd600;
  cursor: pointer;
}

.rating > label::before {
  content: "\2605";
  position: absolute;
  opacity: 0;
}

.rating > label:hover:before,
.rating > label:hover ~ label:before {
  opacity: 1 !important;
}

.rating > input:checked ~ label:before {
  opacity: 1;
}

.rating:hover > input:checked ~ label:before {
  opacity: 0.4;
}

.buttons {
  top: 36px;
  position: relative;
}

.rating-submit {
  border-radius: 15px;
  color: #fff;
  height: 49px;
}

.rating-submit:hover {
  color: #fff;
}
</style>
