<template>
  <div class="row d-flex flex-row mr-2 pr-2">
    <div class="col-md-12 col-sm-6">
      <GMapMap
        :center="center"
        :zoom="14"
        ref="myMapRef"
        map-type-id="terrain"
        style="width: 100vw; height: 30rem"
      >
        <GMapCluster :zoomOnClick="true">
          <GMapMarker
            :key="index"
            v-for="(m, index) in markers"
            :position="m.position"
            :clickable="true"
            :draggable="true"
            :icon="{
              url:
                'data:image/jpeg;base64,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',
              scaledSize: { width: 45, height: 40 },
              labelOrigin: { x: 0, y: 0 },
            }"
            @click="center = m.position"
          />
        </GMapCluster>
      </GMapMap>
    </div>
    <div class="col-md-12 col-sm-6">
      <GMapAutocomplete
        disabled
        v-show="isAuthenticated"
        placeholder="Where to?"
        @place_changed="setPlace"
        :options="{
          bounds: { north: 1.4, south: 1.2, east: 104, west: 102 },
          strictBounds: true,
        }"
        class="form-control"
        style="margin-right: 10%;margin-left: 2%;"
      >
      </GMapAutocomplete>
      <h5 class="form-control ml-6 alert-info" v-show="!isAuthenticated">
        You're not logged in! Please login to request rides.
      </h5>
    </div>
    <div
      class="col-md-6 col-sm-6"
      style="margin-right: 10%;margin-left: 2%;"
      v-show="isAuthenticated"
    >
      <ul class="list-group">
        <li
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          Lela
          <span class="badge bg-primary rounded-pill"
            ><i class="far fa-arrow-right"></i
          ></span>
        </li>
        <li
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          Nyawita
          <span class="badge bg-primary rounded-pill"
            ><i class="far fa-arrow-right"></i
          ></span>
        </li>
      </ul>
    </div>
  </div>
  <div>
    <b-button v-b-modal.modal-1>Launch demo modal</b-button>

    <b-modal id="modal-1" title="BootstrapVue">
      <p class="my-4">Hello from modal!</p>
    </b-modal>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isAuthenticated: true,
      center: { lat: -0.0166666, lng: 34.5999976 },
      markers: [
        {
          position: {
            lat: -0.0166666,
            lng: 34.5999976,
          },
        },
        {
          position: {
            lat: -0.01026666,
            lng: 34.5999976,
          },
        },
        {
          position: {
            lat: -0.0126666,
            lng: 34.610001,
          },
        },
      ],
    };
  },
  mounted() {
    console.log(localStorage.getItem("token"));
    if (localStorage.getItem("token") != null) {
      isAuthenticated = true;
    } else {
      isAuthenticated = false;
    }
    this.$refs.myMapRef.$mapPromise.then((map) => {
      // Create the DIV to hold the control and call the CenterControl()
      // constructor passing in this DIV.
      const centerControlDiv = document.createElement("div");
      this.addCenterControl(centerControlDiv, map);
      map.controls[google.maps.ControlPosition.TOP_CENTER].push(
        centerControlDiv
      );
    });
  },
  methods: {
    setPlace() {},
    addCenterControl(controlDiv, map) {
      const controlUI = document.createElement("div");

      controlUI.innerHTML = `
        <div style="color: white; background: green; padding: 1rem;float:left;">
          Near by Rides
        </div>
      `;

      controlDiv.appendChild(controlUI);
      controlUI.addEventListener("click", () => {
        // Do what ever you want to happen on click event
        map.setCenter({
          lat: -0.016666,
          lng: 34.5999978,
        });
      });
    },
  },
};
</script>

<style>
body {
  margin: 0;
}
</style>
