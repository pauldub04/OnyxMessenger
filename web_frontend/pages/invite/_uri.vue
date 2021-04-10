<template>
  <v-app>
    <v-row no-gutters>
      <NavigationDrawer
        :username="$store.state.user.username"
        :email="$store.state.user.email"
      ></NavigationDrawer>

      <v-container>
        <v-content>
          <v-row class="mt-5">
            <h3>Вступить в чат</h3>
          </v-row>
          <v-row class="mt-5">
            <v-btn>Вступить</v-btn>
          </v-row>
        </v-content>
      </v-container>
    </v-row>
  </v-app>
</template>

<script>
/* eslint-disable */
export default {
  data: () => ({}),
  mounted() {

  },
  methods: {},
}
</script>

