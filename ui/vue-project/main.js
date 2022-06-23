import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueSweetalert2 from 'vue-sweetalert2';
//import * as VueGoogleMaps from "vue2-google-maps";
import VueGoogleMaps from '@fawmi/vue-google-maps'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
window.$headers = {
    Authorization: `Token ` + localStorage.getItem("token"),
};

createApp(App).use(store).use(router, axios).use(VueSweetalert2).use(VueGoogleMaps, {
    load: {
        key: "AIzaSyAIH4XrdSkwiQlakBvmQMyKtqhwvLyeHeQ", // AIzaSyAbvyBxmMbFhrzP9Z8moyYr6dCr-pzjhBE
        libraries: "places"
    },
    installComponents: true,
    autobindAllEvents: true,
}).mount('#app')