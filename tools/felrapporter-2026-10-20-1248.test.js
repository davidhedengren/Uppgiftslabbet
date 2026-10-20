'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermatf1.js','utf8'),c);const bank=Object.values(c.window)[0];
test('Geometriska ändringshastigheter stämmer med förändring av area, volym och omkrets',()=>{
 const h=1e-4;
 const cases=[['3.44',t=>Math.PI*((16+.6*t)/2)**2],['3.20',t=>Math.PI*(6+.4*t)**2],['3.45',t=>4/3*Math.PI*(5+.2*t)**3],['3.79',t=>2*Math.PI*(1-.12*t)]];
 for(const [id,quantity]of cases){const derivative=(quantity(h)-quantity(-h))/(2*h),expected=bank.find(q=>q.id===id).rättSvar;assert.ok(Math.abs(Math.abs(derivative)-expected)<1e-7,id);if(id==='3.79')assert.ok(derivative<0);else assert.ok(derivative>0);}
});
