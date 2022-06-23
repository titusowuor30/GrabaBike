<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Log in</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <select
              class="browser-default custom-select"
              v-model="loggedstatus"
            >
              <option selected>{{ loggedstatus }}</option>
              <option value="Client">Client</option>
              <option value="Rider">Rider</option>
            </select>
          </div>
          <div class="field">
            <label>Username</label>
            <div class="control">
              <input
                type="text"
                name="username"
                class="input"
                v-model="username"
              />
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input
                type="password"
                name="password"
                class="input"
                v-model="password"
              />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "LogIn",
  data() {
    return {
      username: "",
      loggedstatus: "As a",
      password: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.$store.commit("setIsLoading", true);
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");

      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("login/", formData)
        .then((response) => {
          const token = response.data.user.token;
          console.log(
            response.data.roles.filter((item) => {
              return (
                item.name
                  .toLowerCase()
                  .indexOf(this.loggedstatus.toLowerCase()) > -1
              );
            })
          );
          if (
            response.data.roles.filter((item) => {
              return (
                item.name
                  .toLowerCase()
                  .indexOf(this.loggedstatus.toLowerCase()) > -1
              );
            }) != ""
          ) {
            console.log(token);
            this.$store.commit("setToken", token);
            localStorage.setItem("loggedstatus", this.loggedstatus);
            localStorage.setItem("loggedout", false);

            console.log(localStorage.getItem("loggedstatus"));

            axios.defaults.headers.common["Authorization"] = "Token " + token;
            localStorage.setItem("token", token);
            this.$store.commit("setUser", {
              id: response.data.user.id,
              username: response.data.user.username,
            });

            localStorage.setItem("username", response.data.user.username);
            localStorage.setItem("userid", response.data.user.id);
            this.$router.push("/");
            window.location.reload();
          } else {
            toast({
              message:
                "" +
                this.loggedstatus +
                " with such credentials not found not found!",
              type: "is-danger",
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: "top-center",
            });
            return;
          }
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else if (error.message) {
            this.errors.push("Something went wrong. Please try again!");
            console.log(error.message);
          }
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
