<!-- eslint-disable -->

<template>
  <v-row no-gutters>
    <NavigationDrawer
      :username="$store.state.user.username"
      :email="$store.state.user.email"
    ></NavigationDrawer>

    <v-container fill-height>
      <v-row>
        <v-col cols="7" class="mx-auto">
          <v-stepper class="ma-0 pa-0" v-model="stepper" vertical>
            <v-card class="pb-5">
              <v-card-title>{{ $t('pages.createChat.label') }}</v-card-title>
              <v-card-subtitle>{{ $t('pages.createChat.newChat') }}</v-card-subtitle>

              <v-stepper-step :complete="stepper > 1" step="1">
                {{ $t('pages.createChat.stepOne.stepLabel') }}
              </v-stepper-step>
              <v-stepper-content step="1">
                <v-radio-group v-model="newChatType" class="ma-0">
                  <v-radio
                    :label="$t('pages.createChat.stepOne.privateMessages')"
                    :value="1"
                  ></v-radio>
                  <v-radio
                    :label="$t('pages.createChat.stepOne.groupChat')"
                    :value="2"
                  ></v-radio>
                </v-radio-group>
                <v-btn
                  :disabled="newChatType === null"
                  tile
                  color="accent"
                  @click="stepper = 2"
                >
                  {{ $t('pages.createChat.continue') }}
                </v-btn>
                <v-btn plain tile to="/main">
                  {{ $t('pages.createChat.cancel') }}
                </v-btn>
              </v-stepper-content>

              <v-stepper-step :complete="stepper > 2" step="2">
                {{ $t('pages.createChat.stepTwo.stepLabel') }}
              </v-stepper-step>
              <v-stepper-content step="2">
                <v-autocomplete v-if="newChatType === 1"
                  v-model="inviteUserName"
                  :items="users"
                  class="mb-3 mr-10"
                  :placeholder="$t('pages.createChat.stepTwo.placeholderOne')"
                  clearable
                  :label="$t('pages.createChat.stepTwo.placeholderOne')"
                ></v-autocomplete>
                <v-autocomplete v-else
                  v-model="inviteUserName"
                  :items="users"
                  chips
                  deletable-chips
                  multiple
                  class="mb-3 mr-10"
                  :placeholder="$t('pages.createChat.stepTwo.placeholderTwo')"
                  clearable
                  :label="$t('pages.createChat.stepTwo.placeholderTwo')"
                ></v-autocomplete>
                
                <v-btn
                  :disabled="inviteUserName === null"
                  tile
                  color="accent"
                  @click="stepper = 3"
                >
                  {{ $t('pages.createChat.continue') }}
                </v-btn>
                <v-btn plain tile @click="stepper = 1; inviteUserName = null">
                  {{ $t('pages.createChat.cancel') }}
                </v-btn>
              </v-stepper-content>

              <v-stepper-step :complete="stepper > 3" step="3">
                {{ $t('pages.createChat.stepThree.stepLabel') }}
              </v-stepper-step>
              <v-stepper-content step="3">
                <v-file-input
                  :label="$t('pages.createChat.stepThree.subLabel')"
                  class="mt-0 ml-0 mb-3 mr-10"
                  v-model="file"
                  prepend-icon="mdi-camera"
                ></v-file-input>

                <v-btn v-if="newChatType == 1"
                  color="primary"
                  tile
                  :disabled="inviteUserName === null"
                  @click="createChat"
                >
                  {{ $t('pages.createChat.createChat') }}
                </v-btn>
                <v-btn v-else 
                  color="accent"
                  tile
                  @click="stepper = 4">
                  {{ $t('pages.createChat.continue') }}
                </v-btn>

                <v-btn plain tile @click="stepper = 2">
                  {{ $t('pages.createChat.cancel') }}
                </v-btn>
              </v-stepper-content>

              <span v-if="newChatType == 2">
                <v-stepper-step :complete="stepper > 4" step="4">
                  {{ $t('pages.createChat.chatName') }}
                </v-stepper-step>
                <v-stepper-content step="4">
                  <v-form v-model="valid">
                    <v-text-field
                      v-model="chatName"
                      :label="$t('pages.createChat.createChat')"
                      :rules="[
                        (v) => !!v || $t('pages.createChat.stepFour.titleRules'),
                      ]"
                      required
                      clearable
                      class="mb-3 mr-10"
                    ></v-text-field>
                  </v-form>
                  <v-btn
                    color="primary"
                    tile
                    :disabled="!valid"
                    @click="createChat"
                  >
                    {{ $t('pages.createChat.createChat') }}
                  </v-btn>
                  <v-btn plain tile @click="stepper = 3">
                    {{ $t('pages.createChat.cancel') }}
                  </v-btn>
                </v-stepper-content>
              </span>
            </v-card>
          </v-stepper>
        </v-col>
      </v-row>
    </v-container>
  </v-row>
</template>

<script>
import NavigationDrawer from '~/components/NavigationDrawer'
export default {
  name: 'CreateChat',
  components: { NavigationDrawer },
  data: () => ({
    stepper: 1,
    newChatType: null,
    inviteUserName: null,
    chatName: null,
    users: [],
    chatType: [
      {
        name: 'Личные сообщения',
        val: 1,
      },
      {
        name: 'Групповой чат',
        val: 2,
      },
    ],

    valid: false,
    file: null,
  }),
  beforeCreate() {
    this.$store.dispatch('middlewareAuthMain')
    this.$store.dispatch('setAuthHeader', this.$store.getters.getToken)
    console.log('set token', this.$store.getters.getToken)
  },
  updated() {
    console.log('set theme')
    this.$store.dispatch('setTheme', this.$i18n)
  },
  mounted() {
    this.getUsers()
  },
  methods: {
    createChat() {
      if (this.newChatType === 1) {
        this.chatName = this.inviteUserName
        const tmp = this.inviteUserName
        this.inviteUserName = []
        this.inviteUserName.push(tmp)
      }

      const formData = new FormData()
      formData.append('image', this.file)
      formData.append('title', this.chatName)
      formData.append('type', this.newChatType)
      formData.append('users', JSON.stringify(this.inviteUserName))

      this.$axios
        .post('http://localhost:8000/api/chats/', formData)
        .then((response) => {
          console.log(response.data)
          this.$router.push('/main')
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getUsers() {
      console.log('getUsers')
      this.$axios
        .get(`http://127.0.0.1:8000/api/users/all/`)
        .then((response) => {
          this.users = response.data.users.filter(
            (u) => u !== this.$store.getters.getUser.username
          )
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>
