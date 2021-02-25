<template>
  <v-main>
    <NavBar></NavBar>
    <NavigationDrawer></NavigationDrawer>
  </v-main>
</template>

<script>
import NavBar from '~/components/NavBar'
import NavigationDrawer from '~/components/NavigationDrawer'
export default {
  components: { NavBar, NavigationDrawer },
}
</script>
