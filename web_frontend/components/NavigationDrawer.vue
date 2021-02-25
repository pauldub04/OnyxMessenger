<template>
  <v-navigation-drawer permanent clipped expand-on-hover class="py-0">
    <v-list dense>
      <v-list-item v-for="item in items" :key="item.title" class="mb-2" link>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.label }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-spacer></v-spacer>
    <v-list dense>
      <v-list-item link>
        <v-list-item-icon>
          <v-icon>mdi-logout</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Выйти из системы</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'NavigationDrawer',
  data() {
    return {
      items: [
        { label: 'Настройки', icon: 'mdi-cog' },
        { label: 'Создать чат', icon: 'mdi-message-text' },
      ],
    }
  },
}
</script>

<style scoped></style>
