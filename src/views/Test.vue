<!--<script setup lang="ts">

import { ref } from 'vue'

import { usePotiah, ScrollView, ScrollComponent } from 'potiah'

const flag = ref(true)
const duration = ref(1.4)

const { scrollTo, potiah, direction, isScrolling } = usePotiah()

const zero = ref<InstanceType<typeof ScrollComponent> | null>(null)
const zero1 = ref<InstanceType<typeof ScrollComponent> | null>(null)
const blank = ref<HTMLElement>()

</script>


<template>  
  <main>
    <ScrollView :duration="duration" css-direction root>
      <ScrollComponent id="top" is="section" class="zero" ref="zero">
        Scroll comp text!!!
      </ScrollComponent>
      <div class="hello">
        <h1>Hello World From Sam</h1>
      </div>

      <div id="sticky" class="second" data-scroll data-scroll-speed="0.2" :data-flag="flag">
        <h1
          data-scroll
          data-scroll-sticky
          data-scroll-target="#sticky"
        >
          Sticky scroll example
        </h1>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
        <p>Placeholders Placeholders</p>
      </div>

      <div class="third">
        <h1>Vertical Parallax scroll</h1>
        <h1>Horizontal Parallax Scroll</h1>
      </div>
      <div id="blank" class="blank" ref="blank"></div>
      <ScrollComponent
        in-view-class="test-in-view-class"
        repeat
        :style="{ height: '25vh', background: 'blue' }"
      >dirty bastard </ScrollComponent>
    </ScrollView>
  </main>
</template>

<script>
</script>

<style>
section {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: xx-large;
}
.hello {
  background-color: red;
  width: 100vw;
  background-image: url("/src/assets/background.png");
  background-size: cover;
  color: rgba(0, 0, 0, 0.745);
}
.third {
  background-color: greenyellow;
}
#sticky {
  background-color: black;
  padding: 50px;
}
.scroll-into-view {
  background-color: black;
  color: white;
}
</style>-->


<script setup>
  import NavBar from "../components/NavBar.vue";
  import Footer from "../components/Footer.vue";
  import { ref, onMounted, onBeforeUnmount } from "vue";
  import { usePotiah, ScrollView, ScrollComponent } from "potiah";

  const flag = ref(true)
  const duration = ref(1.4)

</script>

<template>
  <main>
    <svg class="hover:fill-black" width="30px" height="30px" viewBox="0 -28.5 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid" fill="#000000">
                        <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                        <g id="SVGRepo_iconCarrier"> <g> <path d="M216.856339,16.5966031 C200.285002,8.84328665 182.566144,3.2084988 164.041564,0 C161.766523,4.11318106 159.108624,9.64549908 157.276099,14.0464379 C137.583995,11.0849896 118.072967,11.0849896 98.7430163,14.0464379 C96.9108417,9.64549908 94.1925838,4.11318106 91.8971895,0 C73.3526068,3.2084988 55.6133949,8.86399117 39.0420583,16.6376612 C5.61752293,67.146514 -3.4433191,116.400813 1.08711069,164.955721 C23.2560196,181.510915 44.7403634,191.567697 65.8621325,198.148576 C71.0772151,190.971126 75.7283628,183.341335 79.7352139,175.300261 C72.104019,172.400575 64.7949724,168.822202 57.8887866,164.667963 C59.7209612,163.310589 61.5131304,161.891452 63.2445898,160.431257 C105.36741,180.133187 151.134928,180.133187 192.754523,160.431257 C194.506336,161.891452 196.298154,163.310589 198.110326,164.667963 C191.183787,168.842556 183.854737,172.420929 176.223542,175.320965 C180.230393,183.341335 184.861538,190.991831 190.096624,198.16893 C211.238746,191.588051 232.743023,181.531619 254.911949,164.955721 C260.227747,108.668201 245.831087,59.8662432 216.856339,16.5966031 Z M85.4738752,135.09489 C72.8290281,135.09489 62.4592217,123.290155 62.4592217,108.914901 C62.4592217,94.5396472 72.607595,82.7145587 85.4738752,82.7145587 C98.3405064,82.7145587 108.709962,94.5189427 108.488529,108.914901 C108.508531,123.290155 98.3405064,135.09489 85.4738752,135.09489 Z M170.525237,135.09489 C157.88039,135.09489 147.510584,123.290155 147.510584,108.914901 C147.510584,94.5396472 157.658606,82.7145587 170.525237,82.7145587 C183.391518,82.7145587 193.761324,94.5189427 193.539891,108.914901 C193.539891,123.290155 183.391518,135.09489 170.525237,135.09489 Z" fill="#FFFFFF" fill-rule="nonzero"> 
                        </path> </g> </g>
                      </svg>
  </main>
</template>

<script>
export default {
  data() {
    return {
      calculatedOpacity: 0,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const scrollPosition = window.scrollY;
      const middleY = window.innerHeight / 2;

      const distanceFromMiddle = Math.abs(scrollPosition - middleY);

      // Adjust the opacity based on the distance from the middle
      this.calculatedOpacity = 1 - distanceFromMiddle / 500;
    },
  },
};
</script>



