function k(){}const ht=t=>t;function mt(t,e){for(const n in e)t[n]=e[n];return t}function et(t){return t()}function V(){return Object.create(null)}function N(t){t.forEach(et)}function G(t){return typeof t=="function"}function Ht(t,e){return t!=t?e==e:t!==e||t&&typeof t=="object"||typeof t=="function"}function pt(t){return Object.keys(t).length===0}function yt(t,...e){if(t==null)return k;const n=t.subscribe(...e);return n.unsubscribe?()=>n.unsubscribe():n}function Gt(t,e,n){t.$$.on_destroy.push(yt(e,n))}function Jt(t,e,n,i){if(t){const s=nt(t,e,n,i);return t[0](s)}}function nt(t,e,n,i){return t[1]&&i?mt(n.ctx.slice(),t[1](i(e))):n.ctx}function Kt(t,e,n,i){if(t[2]&&i){const s=t[2](i(n));if(e.dirty===void 0)return s;if(typeof s=="object"){const o=[],r=Math.max(e.dirty.length,s.length);for(let l=0;l<r;l+=1)o[l]=e.dirty[l]|s[l];return o}return e.dirty|s}return e.dirty}function Qt(t,e,n,i,s,o){if(s){const r=nt(e,n,i,o);t.p(r,s)}}function Ut(t){if(t.ctx.length>32){const e=[],n=t.ctx.length/32;for(let i=0;i<n;i++)e[i]=-1;return e}return-1}function Vt(t){return t&&G(t.destroy)?t.destroy:k}const it=typeof window<"u";let gt=it?()=>window.performance.now():()=>Date.now(),J=it?t=>requestAnimationFrame(t):k;const E=new Set;function rt(t){E.forEach(e=>{e.c(t)||(E.delete(e),e.f())}),E.size!==0&&J(rt)}function wt(t){let e;return E.size===0&&J(rt),{promise:new Promise(n=>{E.add(e={c:t,f:n})}),abort(){E.delete(e)}}}let W=!1;function bt(){W=!0}function xt(){W=!1}function vt(t,e,n,i){for(;t<e;){const s=t+(e-t>>1);n(s)<=i?t=s+1:e=s}return t}function $t(t){if(t.hydrate_init)return;t.hydrate_init=!0;let e=t.childNodes;if(t.nodeName==="HEAD"){const c=[];for(let u=0;u<e.length;u++){const _=e[u];_.claim_order!==void 0&&c.push(_)}e=c}const n=new Int32Array(e.length+1),i=new Int32Array(e.length);n[0]=-1;let s=0;for(let c=0;c<e.length;c++){const u=e[c].claim_order,_=(s>0&&e[n[s]].claim_order<=u?s+1:vt(1,s,a=>e[n[a]].claim_order,u))-1;i[c]=n[_]+1;const f=_+1;n[f]=c,s=Math.max(f,s)}const o=[],r=[];let l=e.length-1;for(let c=n[s]+1;c!=0;c=i[c-1]){for(o.push(e[c-1]);l>=c;l--)r.push(e[l]);l--}for(;l>=0;l--)r.push(e[l]);o.reverse(),r.sort((c,u)=>c.claim_order-u.claim_order);for(let c=0,u=0;c<r.length;c++){for(;u<o.length&&r[c].claim_order>=o[u].claim_order;)u++;const _=u<o.length?o[u]:null;t.insertBefore(r[c],_)}}function st(t,e){t.appendChild(e)}function ot(t){if(!t)return document;const e=t.getRootNode?t.getRootNode():t.ownerDocument;return e&&e.host?e:t.ownerDocument}function Et(t){const e=Q("style");return kt(ot(t),e),e.sheet}function kt(t,e){return st(t.head||t,e),e.sheet}function Nt(t,e){if(W){for($t(t),(t.actual_end_child===void 0||t.actual_end_child!==null&&t.actual_end_child.parentNode!==t)&&(t.actual_end_child=t.firstChild);t.actual_end_child!==null&&t.actual_end_child.claim_order===void 0;)t.actual_end_child=t.actual_end_child.nextSibling;e!==t.actual_end_child?(e.claim_order!==void 0||e.parentNode!==t)&&t.insertBefore(e,t.actual_end_child):t.actual_end_child=e.nextSibling}else(e.parentNode!==t||e.nextSibling!==null)&&t.appendChild(e)}function Xt(t,e,n){W&&!n?Nt(t,e):(e.parentNode!==t||e.nextSibling!=n)&&t.insertBefore(e,n||null)}function K(t){t.parentNode.removeChild(t)}function Q(t){return document.createElement(t)}function St(t){return document.createElementNS("http://www.w3.org/2000/svg",t)}function U(t){return document.createTextNode(t)}function Yt(){return U(" ")}function Zt(){return U("")}function X(t,e,n,i){return t.addEventListener(e,n,i),()=>t.removeEventListener(e,n,i)}function te(t,e,n){n==null?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}function At(t){return Array.from(t.childNodes)}function Mt(t){t.claim_info===void 0&&(t.claim_info={last_index:0,total_claimed:0})}function ct(t,e,n,i,s=!1){Mt(t);const o=(()=>{for(let r=t.claim_info.last_index;r<t.length;r++){const l=t[r];if(e(l)){const c=n(l);return c===void 0?t.splice(r,1):t[r]=c,s||(t.claim_info.last_index=r),l}}for(let r=t.claim_info.last_index-1;r>=0;r--){const l=t[r];if(e(l)){const c=n(l);return c===void 0?t.splice(r,1):t[r]=c,s?c===void 0&&t.claim_info.last_index--:t.claim_info.last_index=r,l}}return i()})();return o.claim_order=t.claim_info.total_claimed,t.claim_info.total_claimed+=1,o}function lt(t,e,n,i){return ct(t,s=>s.nodeName===e,s=>{const o=[];for(let r=0;r<s.attributes.length;r++){const l=s.attributes[r];n[l.name]||o.push(l.name)}o.forEach(r=>s.removeAttribute(r))},()=>i(e))}function ee(t,e,n){return lt(t,e,n,Q)}function ne(t,e,n){return lt(t,e,n,St)}function Ct(t,e){return ct(t,n=>n.nodeType===3,n=>{const i=""+e;if(n.data.startsWith(i)){if(n.data.length!==i.length)return n.splitText(i.length)}else n.data=i},()=>U(e),!0)}function ie(t){return Ct(t," ")}function re(t,e){e=""+e,t.wholeText!==e&&(t.data=e)}function se(t,e,n,i){n===null?t.style.removeProperty(e):t.style.setProperty(e,n,i?"important":"")}let O;function jt(){if(O===void 0){O=!1;try{typeof window<"u"&&window.parent&&window.parent.document}catch{O=!0}}return O}function oe(t,e){getComputedStyle(t).position==="static"&&(t.style.position="relative");const i=Q("iframe");i.setAttribute("style","display: block; position: absolute; top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; border: 0; opacity: 0; pointer-events: none; z-index: -1;"),i.setAttribute("aria-hidden","true"),i.tabIndex=-1;const s=jt();let o;return s?(i.src="data:text/html,<script>onresize=function(){parent.postMessage(0,'*')}<\/script>",o=X(window,"message",r=>{r.source===i.contentWindow&&e()})):(i.src="about:blank",i.onload=()=>{o=X(i.contentWindow,"resize",e)}),st(t,i),()=>{(s||o&&i.contentWindow)&&o(),K(i)}}function ce(t,e,n){t.classList[n?"add":"remove"](e)}function zt(t,e,{bubbles:n=!1,cancelable:i=!1}={}){const s=document.createEvent("CustomEvent");return s.initCustomEvent(t,n,i,e),s}const R=new Map;let B=0;function Ot(t){let e=5381,n=t.length;for(;n--;)e=(e<<5)-e^t.charCodeAt(n);return e>>>0}function Pt(t,e){const n={stylesheet:Et(e),rules:{}};return R.set(t,n),n}function Y(t,e,n,i,s,o,r,l=0){const c=16.666/i;let u=`{
`;for(let p=0;p<=1;p+=c){const g=e+(n-e)*o(p);u+=p*100+`%{${r(g,1-g)}}
`}const _=u+`100% {${r(n,1-n)}}
}`,f=`__svelte_${Ot(_)}_${l}`,a=ot(t),{stylesheet:h,rules:d}=R.get(a)||Pt(a,t);d[f]||(d[f]=!0,h.insertRule(`@keyframes ${f} ${_}`,h.cssRules.length));const y=t.style.animation||"";return t.style.animation=`${y?`${y}, `:""}${f} ${i}ms linear ${s}ms 1 both`,B+=1,f}function Dt(t,e){const n=(t.style.animation||"").split(", "),i=n.filter(e?o=>o.indexOf(e)<0:o=>o.indexOf("__svelte")===-1),s=n.length-i.length;s&&(t.style.animation=i.join(", "),B-=s,B||Lt())}function Lt(){J(()=>{B||(R.forEach(t=>{const{ownerNode:e}=t.stylesheet;e&&K(e)}),R.clear())})}let C;function M(t){C=t}function ut(){if(!C)throw new Error("Function called outside component initialization");return C}function le(t){ut().$$.on_mount.push(t)}function ue(t){ut().$$.after_update.push(t)}const A=[],Z=[],D=[],tt=[],at=Promise.resolve();let H=!1;function ft(){H||(H=!0,at.then(dt))}function ae(){return ft(),at}function T(t){D.push(t)}const F=new Set;let P=0;function dt(){const t=C;do{for(;P<A.length;){const e=A[P];P++,M(e),Rt(e.$$)}for(M(null),A.length=0,P=0;Z.length;)Z.pop()();for(let e=0;e<D.length;e+=1){const n=D[e];F.has(n)||(F.add(n),n())}D.length=0}while(A.length);for(;tt.length;)tt.pop()();H=!1,F.clear(),M(t)}function Rt(t){if(t.fragment!==null){t.update(),N(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(T)}}let S;function Bt(){return S||(S=Promise.resolve(),S.then(()=>{S=null})),S}function I(t,e,n){t.dispatchEvent(zt(`${e?"intro":"outro"}${n}`))}const L=new Set;let x;function fe(){x={r:0,c:[],p:x}}function de(){x.r||N(x.c),x=x.p}function _t(t,e){t&&t.i&&(L.delete(t),t.i(e))}function Tt(t,e,n,i){if(t&&t.o){if(L.has(t))return;L.add(t),x.c.push(()=>{L.delete(t),i&&(n&&t.d(1),i())}),t.o(e)}else i&&i()}const Wt={duration:0};function _e(t,e,n,i){let s=e(t,n),o=i?0:1,r=null,l=null,c=null;function u(){c&&Dt(t,c)}function _(a,h){const d=a.b-o;return h*=Math.abs(d),{a:o,b:a.b,d,duration:h,start:a.start,end:a.start+h,group:a.group}}function f(a){const{delay:h=0,duration:d=300,easing:y=ht,tick:p=k,css:g}=s||Wt,v={start:gt()+h,b:a};a||(v.group=x,x.r+=1),r||l?l=v:(g&&(u(),c=Y(t,o,a,d,h,y,g)),a&&p(0,1),r=_(v,d),T(()=>I(t,a,"start")),wt($=>{if(l&&$>l.start&&(r=_(l,d),l=null,I(t,r.b,"start"),g&&(u(),c=Y(t,o,r.b,r.duration,0,y,s.css))),r){if($>=r.end)p(o=r.b,1-o),I(t,r.b,"end"),l||(r.b?u():--r.group.r||N(r.group.c)),r=null;else if($>=r.start){const j=$-r.start;o=r.a+r.d*y(j/r.duration),p(o,1-o)}}return!!(r||l)}))}return{run(a){G(s)?Bt().then(()=>{s=s(),f(a)}):f(a)},end(){u(),r=l=null}}}function he(t,e){Tt(t,1,1,()=>{e.delete(t.key)})}function me(t,e,n,i,s,o,r,l,c,u,_,f){let a=t.length,h=o.length,d=a;const y={};for(;d--;)y[t[d].key]=d;const p=[],g=new Map,v=new Map;for(d=h;d--;){const m=f(s,o,d),w=n(m);let b=r.get(w);b?i&&b.p(m,e):(b=u(w,m),b.c()),g.set(w,p[d]=b),w in y&&v.set(w,Math.abs(d-y[w]))}const $=new Set,j=new Set;function q(m){_t(m,1),m.m(l,_),r.set(m.key,m),_=m.first,h--}for(;a&&h;){const m=p[h-1],w=t[a-1],b=m.key,z=w.key;m===w?(_=m.first,a--,h--):g.has(z)?!r.has(b)||$.has(b)?q(m):j.has(z)?a--:v.get(b)>v.get(z)?(j.add(b),q(m)):($.add(z),a--):(c(w,r),a--)}for(;a--;){const m=t[a];g.has(m.key)||c(m,r)}for(;h;)q(p[h-1]);return p}function pe(t){t&&t.c()}function ye(t,e){t&&t.l(e)}function qt(t,e,n,i){const{fragment:s,on_mount:o,on_destroy:r,after_update:l}=t.$$;s&&s.m(e,n),i||T(()=>{const c=o.map(et).filter(G);r?r.push(...c):N(c),t.$$.on_mount=[]}),l.forEach(T)}function Ft(t,e){const n=t.$$;n.fragment!==null&&(N(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}function It(t,e){t.$$.dirty[0]===-1&&(A.push(t),ft(),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function ge(t,e,n,i,s,o,r,l=[-1]){const c=C;M(t);const u=t.$$={fragment:null,ctx:null,props:o,update:k,not_equal:s,bound:V(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(e.context||(c?c.$$.context:[])),callbacks:V(),dirty:l,skip_bound:!1,root:e.target||c.$$.root};r&&r(u.root);let _=!1;if(u.ctx=n?n(t,e.props||{},(f,a,...h)=>{const d=h.length?h[0]:a;return u.ctx&&s(u.ctx[f],u.ctx[f]=d)&&(!u.skip_bound&&u.bound[f]&&u.bound[f](d),_&&It(t,f)),a}):[],u.update(),_=!0,N(u.before_update),u.fragment=i?i(u.ctx):!1,e.target){if(e.hydrate){bt();const f=At(e.target);u.fragment&&u.fragment.l(f),f.forEach(K)}else u.fragment&&u.fragment.c();e.intro&&_t(t.$$.fragment),qt(t,e.target,e.anchor,e.customElement),xt(),dt()}M(c)}class we{$destroy(){Ft(this,1),this.$destroy=k}$on(e,n){const i=this.$$.callbacks[e]||(this.$$.callbacks[e]=[]);return i.push(n),()=>{const s=i.indexOf(n);s!==-1&&i.splice(s,1)}}$set(e){this.$$set&&!pt(e)&&(this.$$.skip_bound=!0,this.$$set(e),this.$$.skip_bound=!1)}}export{k as A,Jt as B,Qt as C,Ut as D,Kt as E,Nt as F,Gt as G,St as H,ne as I,T as J,ce as K,oe as L,me as M,Vt as N,G as O,_e as P,he as Q,Z as R,we as S,Yt as a,Xt as b,ie as c,de as d,Zt as e,_t as f,fe as g,K as h,ge as i,ue as j,Q as k,ee as l,At as m,te as n,le as o,se as p,U as q,Ct as r,Ht as s,Tt as t,re as u,pe as v,ye as w,qt as x,Ft as y,ae as z};