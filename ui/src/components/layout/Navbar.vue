<template>
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <strong>Easy Rides</strong>
      </router-link>
    </div>

    <div class="navbar-menu">
      <div class="navbar-end">
        <template v-if="$store.state.isAuthenticated">
          <router-link
            to="/dashboard/leads"
            class="navbar-item"
            v-show="isRider"
            >Ride Leads</router-link
          >
          <router-link
            to="/dashboard/clients"
            class="navbar-item"
            v-show="isRider"
            >Frequent Clients</router-link
          >
          <router-link to="/dashboard/team" class="navbar-item" v-show="isRider"
            >Subscriptions</router-link
          >
        </template>

        <div class="navbar-item">
          <div class="buttons">
            <template v-if="!$store.state.isAuthenticated">
              <router-link to="/sign-up" class="button is-success"
                ><strong>Sign up</strong></router-link
              >
              <router-link to="/log-in" class="button is-light"
                >Log in</router-link
              >
            </template>

            <template v-else>
              <router-link to="/dashboard/my-account" class="button is-info"
                >My account</router-link
              >
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      isRider: false,
    };
  },
  created() {
    if (localStorage.getItem("loggedstatus") === "Client") {
      this.isRider = false;
    } else {
      this.isRider = true;
    }
  },
  mounted() {
    if (localStorage.getItem("loggedstatus") === "Client") {
      this.isRider = false;
    } else {
      this.isRider = true;
    }
  },
};
</script>
