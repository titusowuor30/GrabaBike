<template>
  <section class="section">
    <div class="container xl">
      <div class="columns is-centered">
        <GoogleMap />
      </div>
    </div>
  </section>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import GoogleMap from "../components/google.vue";

export default {
  name: "Home",
  components: {
    HelloWorld,
    GoogleMap,
  },
  mounted() {
    console.log(JSON.stringify(localStorage.getItem("user")).username);
  },
};
</script>
