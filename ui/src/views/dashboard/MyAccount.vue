<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My account</h1>
      </div>

      <div class="column is-12">
        <div class="buttons">
          <router-link
            :to="{ name: 'EditMember', params: { id: $store.state.user.id } }"
            class="button is-light"
            >Edit</router-link
          >

          <button @click="logout()" class="button is-danger">Log out</button>
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Ride History</h1>

        <router-link
          to="/dashboard/leads/add"
          v-if="$store.state.team.max_leads > num_leads"
          >Add lead</router-link
        >

        <div class="notification is-danger" v-else>
          You have reached the top of your limitations. Please upgrade!
        </div>

        <hr />

        <form @submit.prevent="getLeads">
          <div class="field has-addons">
            <div class="control">
              <input type="text" class="input" v-model="query" />
            </div>
            <div class="control">
              <button class="button is-success">Search</button>
            </div>
          </div>
        </form>
      </div>

      <div class="column is-12">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Source</th>
              <th>Destination</th>
              <th v-if="!isRider">Rider</th>
              <th v-else>Client</th>
              <th>Phone</th>
              <th>Confirmed</th>
              <th>Rating</th>
              <th>Completed</th>
              <th class="m-auto">
                Action
              </th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="(ride, index) in rides" :key="ride">
              <td>
                {{ ride.sorce }}
              </td>
              <td>
                {{ ride.destination }}
              </td>
              <td>
                {{ users[index].username }}
              </td>
              <td>{{ users[index].tel }}</td>
              <td>
                <div class="form-check m-auto">
                  <input
                    class="form-check-input m-auto"
                    type="checkbox"
                    value=""
                    id="flexCheckChecked"
                    :checked="ride.confirmed"
                  />
                </div>
              </td>
              <td>
                {{ ride.rating }}
              </td>
              <td>
                <div class="form-check m-auto">
                  <input
                    class="form-check-input m-auto"
                    type="checkbox"
                    value=""
                    id="flexCheckChecked"
                    :checked="ride.completed"
                  />
                </div>
              </td>
              <td>
                <div class="d-inline" v-show="isRider">
                  <button
                    type="button"
                    class="btn btn-primary"
                    data-bs-toggle="modal"
                    data-bs-target="#completRide"
                    v-show="!isRider && ride.confirmed && !ride.completed"
                  >
                    Complete Ride</button
                  >&nbsp;
                  <button
                    type="button"
                    class="btn btn-success"
                    v-show="isRider && !ride.confirmed && !ride.completed"
                    @click="
                      confirmRide(ride.rider, users[index].username, 'accept')
                    "
                  >
                    Accept</button
                  >&nbsp;
                  <button
                    type="button"
                    class="btn btn-danger"
                    v-show="isRider && ride.confirmed && !ride.completed"
                    @click="
                      confirmRide(ride.rider, users[index].username, 'cancel')
                    "
                  >
                    Cancel
                  </button>
                  <div class="container">
                    <!-- Modal -->
                    <div
                      class="modal fade"
                      id="completRide"
                      tabindex="-1"
                      aria-labelledby="exampleModalLabel"
                      aria-hidden="true"
                    >
                      <div class="modal-dialog">
                        <div class="modal-content">
                          <div class="modal-header">
                            <h5
                              class="modal-title text-danger"
                              id="exampleModalLabel"
                            >
                              Complete
                              <span class="text-info"
                                >{{ ride.sorce }}-{{ ride.destination }}</span
                              >
                              Ride(#id:{{ ride.id }})
                            </h5>
                            <button
                              type="button"
                              class="btn-close"
                              data-bs-dismiss="modal"
                              aria-label="Close"
                            ></button>
                          </div>
                          <div class="modal-body">
                            <form
                              @submit.prevent="
                                completeRide(
                                  ride.id,
                                  ride.rider,
                                  users[index].username
                                )
                              "
                            >
                              <div class="mb-3">
                                <div class="field">
                                  <select
                                    class="browser-default custom-select"
                                    v-model="paymethod"
                                    @change="hidefield()"
                                  >
                                    <option
                                      value="Select Payment Method"
                                      selected
                                      >{{ paymethod }}</option
                                    >
                                    <option value="Cash">Cash</option>
                                    <option value="Mpesa">Mpesa</option>
                                  </select>
                                </div>
                                <div class="" v-show="ishide">
                                  <label
                                    for="exampleInputEmail1"
                                    class="form-label"
                                    v-show="ishide"
                                    >Transaction Code:</label
                                  >
                                  <input
                                    v-show="ishide"
                                    type="text"
                                    class="form-control"
                                    id="exampleInputEmail1"
                                    aria-describedby="emailHelp"
                                    v-model="trcode"
                                    required
                                  />
                                </div>
                              </div>
                              <div class="mb-3">
                                <label
                                  for="exampleInputPassword1"
                                  class="form-label"
                                  >Amount:</label
                                >
                                <input
                                  type="text"
                                  class="form-control"
                                  id="exampleInputPassword1"
                                  placeholder="50.00"
                                  v-model="amount"
                                  required
                                />
                              </div>
                              <div class="mb-3">
                                <div class="field">
                                  <select
                                    class="browser-default custom-select"
                                    v-model="rating"
                                  >
                                    <option value="Ride Rating" selected>{{
                                      rating
                                    }}</option>
                                    <option value="1">Poor</option>
                                    <option value="2">Fair</option>
                                    <option value="3">Good</option>
                                    <option value="4">Better</option>
                                    <option value="5">Excellent</option>
                                  </select>
                                </div>
                                <label
                                  for="exampleInputPassword1"
                                  class="form-label"
                                  >Comments:</label
                                >
                                <input
                                  type="text"
                                  class="form-control"
                                  id="exampleInputPassword1"
                                  placeholder="Quick comment"
                                  v-model="comments"
                                />
                              </div>
                              <button type="submit" class="btn btn-primary">
                                submit
                              </button>
                            </form>
                          </div>
                          <div class="modal-footer">
                            <button
                              type="button"
                              class="btn btn-warning"
                              data-bs-dismiss="modal"
                            >
                              Close
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>

        <div class="buttons">
          <button
            class="button is-light"
            @click="goToPreviousPage()"
            v-if="showPreviousButton"
          >
            Previous
          </button>
          <button
            class="button is-light"
            @click="goToNextPage()"
            v-if="showNextButton"
          >
            Next
          </button>
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
  name: "MyAccount",
  data() {
    return {
      rides: [],
      isRider: false,
      ishide: true,
      users: [],
      userid: "",
      paymethod: "Select Payment Method",
      rating: "Ride Rating",
      comments: "",
      amount: 0.0,
      trcode: "Cash",
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      query: "",
    };
  },
  created() {
    this.hidefield();
    if (localStorage.getItem("loggedstatus") != "Client") {
      this.isRider = true;
    }
  },
  mounted() {
    this.getHistory();
    this.hidefield();
    console.log(localStorage.getItem("loggedstatus"));
    if (localStorage.getItem("loggedstatus") != "Client") {
      this.isRider = true;
    }
  },
  methods: {
    hidefield() {
      if (this.paymethod === "Cash") {
        ishide = false;
      }
    },
    logout() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("user");
      localStorage.removeItem("userid");
      localStorage.removeItem("team_name");
      localStorage.removeItem("team_id");
      this.$store.commit("removeToken");
      this.$router.push("/");
      localStorage.setItem("loggedout", true);
      window.location.reload();
    },
    async completeRide(rideid, rider, client) {
      this.$store.commit("setIsLoading", true);
      const data = {
        rideid: rideid,
        rider: rider,
        client: client,
        paymethod: this.paymethod,
        trcode: this.trcode,
        amount: this.amount,
        rating: this.rating,
        comments: this.comments,
      };
      console.log(data);
      await axios
        .post(`rides/complete_ride/`, data)
        .then((response) => {
          console.log(response.data);
          toast({
            message: response.data.toString(),
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: "top-center",
          });
          window.location.reload();
        })
        .catch((e) => {
          toast({
            message: e.toString(),
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: "top-center",
          });
        });
      this.$store.commit("setIsLoading", false);
    },
    async confirmRide(riderid, client, command) {
      this.$store.commit("setIsLoading", true);
      const data = { riderid: riderid, client: client, command };
      console.log(data);
      await axios
        .post(`rides/confirm_ride/`, data)
        .then((response) => {
          console.log(response.data);
          toast({
            message: response.data.toString(),
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: "top-center",
          });
          window.location.reload();
        })
        .catch((e) => {
          toast({
            message: e.toString(),
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: "top-center",
          });
        });
      this.$store.commit("setIsLoading", false);
    },
    async getHistory() {
      this.$store.commit("setIsLoading", true);

      this.showNextButton = false;
      this.showPreviousButton = false;

      await axios.get(`rides/`).then((response) => {
        if (localStorage.getItem("loggedstatus") === "Client") {
          console.log(
            response.data.filter((item) => {
              return item.client == localStorage.getItem("userid");
            })
          );
          this.rides = response.data.filter((item) => {
            return item.client == localStorage.getItem("userid");
          });
        } else {
          console.log(response.data);
          this.rides = response.data;
        }
        if (this.isRider) {
          for (var i = 0; i < this.rides.length; i++) {
            //console.log(this.riders[i].id);
            axios.get("listusers/" + response.data[i].client).then((res) => {
              console.log(res.data);
              this.users.push({
                username: res.data.username,
                first_name: res.data.first_name,
                last_name: res.data.last_name,
                tel: res.data.tel,
              });
            });
          }
        } else {
          for (var i = 0; i < this.rides.length; i++) {
            //console.log(this.riders[i].id);
            axios
              .get("riders/" + response.data[i].rider)
              .then((res) => {
                console.log(res.data.user);
                this.userid = res.data.user;
              })
              .then(() => {
                axios.get("listusers/" + this.userid).then((res) => {
                  console.log(res.data);
                  this.users.push({
                    username: res.data.username,
                    first_name: res.data.first_name,
                    last_name: res.data.last_name,
                    tel: res.data.tel,
                  });
                });
              });
          }
        }
        //console.log(this.riders[i].id);

        console.log(this.users);
      });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
