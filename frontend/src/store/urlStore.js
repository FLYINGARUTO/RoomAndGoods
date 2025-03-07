import { defineStore } from "pinia";

export const useUrlStore = defineStore("urlStore", {
    state: () => ({
        baseUrl: `${window.location.protocol}//${window.location.hostname}:8000`,
    }),
    actions: {
        setUrl(url) {
            this.baseUrl = url;
        }
    }
});
