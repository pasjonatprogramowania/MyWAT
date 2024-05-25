<template>
  <div class="q-pa-lg">
    <h5>Opcje</h5>
    <q-list bordered class="prounded-borders">
      <q-expansion-item
        expand-separator
        icon="event"
        label="Typ wydarzenia"
      >
        <q-option-group
          v-model="group"
          :options="options"
          color="primary"
          class="q-pa-sm"
          type="checkbox"
        />
      </q-expansion-item>
    </q-list>
    <q-expansion-item
      expand-separator
      icon="place"

      label="Dodawanie punktów"
    >
      <div class="q-pa-sm">


      <q-btn
        color="primary"
        text-color="white"
        label="Dodaj"
        @click="addDialogShow()"
      />
      <q-btn
        color="primary"
        text-color="white"
        label="Usuń"
        @click="removeDialogShow()"
      />
      <q-btn
        color="primary"
        text-color="white"
        label="Popraw"
        @click="editDialogShow()"
      />
      </div>
    </q-expansion-item>
    <q-expansion-item class="q-pa-sm" expand-separator icon="local_shipping" label="Przejazdy">
      <TimeInput></TimeInput>
      <q-btn color="primary" text-color="white" label="Pokaż" @click="driveShow()" />
    </q-expansion-item>
  </div>
  <q-dialog v-model="isAddDialogShow" no-esc-dismiss no-backdrop-dismiss>
   <q-card>
    <q-card-section>
      <h5>Dodaj Punkt</h5>
      <div>
        <q-input v-model="objToSend.name" label="Nazwa" ></q-input>
        <q-input v-model="objToSend.description" label="Opis" ></q-input>
        <q-input v-model="objToSend.link" label="Link" ></q-input>
        <q-input v-model="objToSend.cordinats[0]" label="Współrzedne (Długość)" ></q-input>
        <q-input v-model="objToSend.cordinats[1]" label="Współrzedne (Szerokość)" ></q-input>
        <div class="q-pa-md" style="max-width: 300px">
          <q-input filled v-model="objToSend.date">
            <template v-slot:prepend>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <q-date v-model="objToSend.date" mask="YYYY-MM-DD HH:mm">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>

            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <q-time v-model="objToSend.date" mask="YYYY-MM-DD HH:mm" format24h>
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>

        <q-checkbox v-model="objToSend.isRecursive" label="Czy jest powtarzalne?"></q-checkbox>
        <q-item >
          <q-item-section v-if="objToSend.isRecursive">
            <q-radio v-model="objToSend.recursiveWeekDay" val="poniedziałek" label="poniedziałek"></q-radio>
            <q-radio v-model="objToSend.recursiveWeekDay" val="wtorek" label="wtorek" ></q-radio>
            <q-radio v-model="objToSend.recursiveWeekDay" val="sroda" label="sroda" ></q-radio>
            <q-radio v-model="objToSend.recursiveWeekDay" val="czwartek" label="czwartek" ></q-radio>
            <q-radio v-model="objToSend.recursiveWeekDay" val="piatek" label="piatek" ></q-radio>
            <q-radio v-model="objToSend.recursiveWeekDay" val="sobota" label="sobota" ></q-radio>
            <q-radio v-model="objToSend.recursiveWeekDay" val="niedziela" label="niedziela" ></q-radio>
          </q-item-section>
        </q-item>
        <q-btn @click="emit('addPoint');addDialogHide()" color="primary">Dodaj punkt</q-btn>
        <q-btn @click="addDialogHide()" color="primary">Zamknij</q-btn>
      </div>
    </q-card-section>
   </q-card>
  </q-dialog>
  <q-dialog v-model="isRemoveDialogShow" no-esc-dismiss no-backdrop-dismiss>
<!--    Dodac v-for który wyswielti wszystkie rzeczy dodane-->
    <q-card>
      <q-card-section>
        <q-list>
          <q-item>Test</q-item>
          <q-btn @click="emit('removePoint');removeDialogHide()"></q-btn>
        </q-list>
      </q-card-section>
    </q-card>
  </q-dialog>
  <q-dialog v-model="isEditDialogShow" no-esc-dismiss no-backdrop-dismiss>
    <!--    Dodac v-for który wyswielti wszystkie rzeczy dodane-->
    <q-list>
      <q-card>
        <q-card-section>
          <q-item>Test</q-item>
          <q-btn @click="emit('correctPoint');editDialogHide()"></q-btn>
        </q-card-section>
      </q-card>
    </q-list>
  </q-dialog>
  <q-dialog v-model="isDriveShow" no-esc-dismiss no-backdrop-dismiss>
    <q-card>
      <!--    Dodac v-for który wyswielti wszystkie rzeczy dodane-->
      <q-card-section>
        <q-item>Test</q-item>
        <q-btn @click="driveHide()"></q-btn>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script setup>
// import { usePointsStore } from 'src/store';
import { ref, defineEmits,onMounted } from "vue";
import TimeInput from "components/TimeInput.vue";

// const pointsStore = usePointsStore()
//
// onMounted(() => {
//   pointsStore.fetchPoints()
// })

const emit = defineEmits(["addPoint", "removePoint", "correctPoint"]);
const group = ref(["kz"]);
let isAddDialogShow = ref(false);
let isRemoveDialogShow = ref(false);
let isEditDialogShow = ref(false);
let isDriveShow = ref(false);
let objToSend = ref({
  name:"",
  description:"",
  link:'',
  location:"",
  cordinats:[],
  date:"",
  isRecursive:false,
  recursiveWeekDay:"",
})
function driveShow(){
  isDriveShow.value = true;
}
function driveHide(){
  isDriveShow.value = false;
}
function addDialogShow(){
  isAddDialogShow.value = true;
}
function addDialogHide(){
  isAddDialogShow.value = false;
}
function removeDialogShow(){
  isRemoveDialogShow.value = true;
}
function removeDialogHide(){
  isRemoveDialogShow.value = false;
}
function editDialogShow(){
  isEditDialogShow.value = true;
}
function editDialogHide(){
  isEditDialogShow.value = false;
}
const options = ref([
  {
    label: "Koła zainteresowań ",
    value: "kz",
  },
  {
    label: "Imprezy eventy watowe",
    value: "iw",
  },
  {
    label: "Ogłoszenia",
    value: "og",
  },
]);
</script>
