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


<!--<script setup>
  import NavBar from "../components/NavBar.vue";
  import Footer from "../components/Footer.vue";
  import { ref, onMounted, onBeforeUnmount } from "vue";
  import { usePotiah, ScrollView, ScrollComponent } from "potiah";

  const flag = ref(true);
  const duration = ref(1.4);

</script>

<template>
  <main>
    <ScrollView :duration="duration" css-direction root>
      <div class="main">
        <div class="w-col"></div>
          <div class="center">
            <div class="py-96 flex flex-col items-center justify-center text-[7.3rem] leading-none opacity-100 animate-fadeup">
              <h1 class="font-kanit ">Looking for a cool Discord Bot? <a class="underline text-blue decoration-white selection:decoration-white" href="#">Invite me</a></h1>
            </div>
            <div class="w-full flex relative z-10" :style="{ opacity: calculatedOpacity }">
              <div class="left">
                <h1 class="text-8xl">Hey, there</h1>
                <p class="my-20">
                  Hello there! I'm Dwello, the newest addition to your Discord community. Ready to bring some cool features to your server and make it an even better place for everyone. Let's get started!
                </p>
                <div class="flex justify-between gap-5">
                  <a href="#">
                    <button class="bg-discord hover:text-discord group mt-8 flex items-center gap-3 rounded-full border-4 border-solid border-[#99aab5] p-4 text-xl font-bold text-white transition-colors duration-300 hover:bg-white hover:border-white">
                      <svg class="group-hover:fill-discord fill-white transition-colors duration-300" width="30px" height="30px" viewBox="0 -28.5 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
                        <path d="M216.856339,16.5966031 C200.285002,8.84328665 182.566144,3.2084988 164.041564,0 C161.766523,4.11318106 159.108624,9.64549908 157.276099,14.0464379 C137.583995,11.0849896 118.072967,11.0849896 98.7430163,14.0464379 C96.9108417,9.64549908 94.1925838,4.11318106 91.8971895,0 C73.3526068,3.2084988 55.6133949,8.86399117 39.0420583,16.6376612 C5.61752293,67.146514 -3.4433191,116.400813 1.08711069,164.955721 C23.2560196,181.510915 44.7403634,191.567697 65.8621325,198.148576 C71.0772151,190.971126 75.7283628,183.341335 79.7352139,175.300261 C72.104019,172.400575 64.7949724,168.822202 57.8887866,164.667963 C59.7209612,163.310589 61.5131304,161.891452 63.2445898,160.431257 C105.36741,180.133187 151.134928,180.133187 192.754523,160.431257 C194.506336,161.891452 196.298154,163.310589 198.110326,164.667963 C191.183787,168.842556 183.854737,172.420929 176.223542,175.320965 C180.230393,183.341335 184.861538,190.991831 190.096624,198.16893 C211.238746,191.588051 232.743023,181.531619 254.911949,164.955721 C260.227747,108.668201 245.831087,59.8662432 216.856339,16.5966031 Z M85.4738752,135.09489 C72.8290281,135.09489 62.4592217,123.290155 62.4592217,108.914901 C62.4592217,94.5396472 72.607595,82.7145587 85.4738752,82.7145587 C98.3405064,82.7145587 108.709962,94.5189427 108.488529,108.914901 C108.508531,123.290155 98.3405064,135.09489 85.4738752,135.09489 Z M170.525237,135.09489 C157.88039,135.09489 147.510584,123.290155 147.510584,108.914901 C147.510584,94.5396472 157.658606,82.7145587 170.525237,82.7145587 C183.391518,82.7145587 193.761324,94.5189427 193.539891,108.914901 C193.539891,123.290155 183.391518,135.09489 170.525237,135.09489 Z"></path>
                      </svg>
                      <span>Add Dwello</span>
                    </button>
                  </a>
                  <a href="#">
                    <button class="text-xl font-bold p-4 mt-8 rounded-full border-4 border-solid border-[#99aab5] text-white flex relative transition-colors duration-300 hover:bg-blue hover:border-blue">
                      <span>Login to Dashboard</span>
                    </button>
                  </a>
                </div>
              </div>
              <div class="right">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
            </div>
            <div class="w-full flex relative z-20" data-scroll data-scroll-speed="0.3" :data-flag="flag">
              <div class="left">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
              <div class="left">
                <h1 class="text-8xl mb-6">Customize your experience</h1>
                <p class="mt-20 mb-[3.25rem]">
                  Elevate your Discord experience with advanced customization options. Tailor outputs, fine-tune server settings, and take control of personal preferences, including the ability to disable intrusive bot DMs. Your Discord, your way – customize effortlessly!
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
            </div>
            <div class="w-full flex relative z-30 -mt-32" data-scroll data-scroll-speed="0.6" :data-flag="flag">
              <div class="left">
                <h1 class="text-8xl">Economy & Market</h1>
                <p class="my-20">
                  Get ready for the Discord-wide party of trading! Jump into the action as you trade unique virtual goodies across servers, tweak trends, and play with prices. It's not just a market; it's an exhilarating global economy waiting for your moves!
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
              <div class="right">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
            </div>
            <div class="w-full flex relative z-40 -mt-52" data-scroll data-scroll-speed="0.9" :data-flag="flag">
              <div class="left">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
              <div class="left">
                <h1 class="text-8xl mb-6">Levelling & Leaderboards</h1>
                <p class="mt-20 mb-12">
                  Level up across servers, snagging cool rewards and climbing leaderboards. And guess what? We've got the annoying notifications turned off by default, so you can enjoy the game without the buzzkill. Ready to dominate the leaderboards? Let the leveling adventure begin! 
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
            </div>
            <div class="w-full flex relative z-50 -mt-72" data-scroll data-scroll-speed="1.2" :data-flag="flag">
              <div class="left">
                <h1 class="text-8xl">Moderation</h1>
                <p class="my-20">
                  Transform your Discord experience with cutting-edge moderation tools. Elevate control, manage content effortlessly, and create a thriving community where conversations flourish.
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
              <div class="right">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
            </div>
            <div class="w-full flex relative z-[60] mt-[-18rem]" data-scroll data-scroll-speed="1.5" :data-flag="flag">
              <div class="left">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
              <div class="left">
                <h1 class="text-8xl mb-6">Other Features</h1>
                <p class="mt-20 mb-12">
                  Unlock a world of possibilities with additional features. From managing to-do lists seamlessly to accessing dynamic API-based commands for movie, weather, and track information, our utility commands empower your Discord server with versatility and convenience. Enhance every interaction and make your community truly extraordinary.
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
            </div>
          </div>
        <div class="w-col"></div>
      </div>
      <div class="z-50 bg-white w-screen h-[60vh]"></div>
    </ScrollView>
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
      console.log(middleY);

      const distanceFromMiddle = Math.abs(scrollPosition - middleY);

      // Adjust the opacity based on the distance from the middle
      this.calculatedOpacity = 1 - distanceFromMiddle / 500;
    },
  },
};
</script>-->

<script setup>
import Footer from "../components/Footer.vue";
  import { ref } from "vue";
  
  let input = ref("");
  const fruits = ["apple", "banana", "orange"];
  function filteredList() {
    return fruits.filter((fruit) =>
      fruit.toLowerCase().includes(input.value.toLowerCase())
    );
  }
</script>

<template>
  <main>
    <div class="main mb-footer"> <!-- use mb-footer if you want to see footer-->
      <div class="w-col"></div>
        <div class="center">
          <h1 class="text-8xl my-28">Welcome to Dwello Docs.</h1>
          <div class="grid grid-cols-1 gap-4 mt-4">
            <div v-for="(value, key) in commands" :key="key" class="p-4 border rounded shadow-md">
              <h1 class="text-lg font-bold">{{ key }}</h1>
              <div v-for="(itemValue, itemKey) in value" :key="itemKey" class="mt-2">
                <h2 class="text-lg font-semibold">{{ itemKey }}</h2>
                <p v-html="formatText(itemValue.help)"></p>
              </div>
            </div>
          </div>
        </div>
      <div class="w-col"></div>
    </div>
    <Footer />
  </main>
</template>

<script>
export default {
  data() {
    return {
      commands: {}
    };
  },
  beforeMount() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      fetch('http://localhost:8081/api/get', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          }
        })
        .then(response => response.json())
        .then(data => {
          this.commands = data;
          console.log(data);
        })
        .catch(error => console.error('Error:', error));
    },
    formatText(text) {
      if (!text) return text;

      // Replace **bold** with <strong>bold</strong>
      text = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

      // Replace __underscores__ with <em>underscores</em>
      text = text.replace(/__(.*?)__/g, "<em>$1</em>");

      // Replace [a link](url) with <a href="url">a link</a>
      //Doesnt remove the <> within (), so cant properly redirect?
      text = text.replace(/\[(.*?)\]\(([^)]+?)\)/g, '<a href="$2">$1</a>');
      console.log(text)

      return text;
    }
  },
};
</script>


<!--<script setup>
import { ref } from "vue";
let input = ref("");
const fruits = ["apple", "banana", "orange"];
function filteredList() {
  return fruits.filter((fruit) =>
    fruit.toLowerCase().includes(input.value.toLowerCase())
  );
}
</script>


<template>
  <input type="text" v-model="input" placeholder="Search fruits..." />
  <div class="item fruit" v-for="fruit in filteredList()" :key="fruit">
    <p>{{ fruit }}</p>
  </div>
  <div class="item error" v-if="input&&!filteredList().length">
    <p>No results found!</p>
  </div>
</template>-->


