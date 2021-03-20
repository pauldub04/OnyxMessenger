export default function ({ store, redirect }) {
  console.log('middleware2, token = ')
  console.log(store.state.token)
  if (store.state.token !== null) {
    return redirect('/main')
  }
}
