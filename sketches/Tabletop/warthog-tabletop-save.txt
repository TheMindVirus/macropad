stateW = 0
stateS = 0
stateA = 0
stateD = 0
frc = 0
trq = 0

function onLoad()
  obj = self.getChild("Warthog(Clone)")
  nod = obj.getChild("Camera_Node")
  cam = nod.getComponent("Camera")
  print(cam)
  print(cam.get("enabled"))
end

function onScriptingButtonDown(index, color)
  obj = self.getChild("Warthog(Clone)")
  nod = obj.getChild("Camera_Node")
  cam = nod.getComponent("Camera")
  isdrivemode = cam.get("enabled")
  physics = obj.getComponent("ConstantForce")
  print(index .. " " .. color .. " " .. tostring(isdrivemode))
  if index == 1 then stateW = 1 end
  if index == 2 then stateA = 1 end
  if index == 3 then stateS = 1 end
  if index == 4 then stateD = 1 end
  local frc_tmp = 0
  if stateW == 1 then frc_tmp = frc_tmp + 1 end
  if stateS == 1 then frc_tmp = frc_tmp - 1 end
  frc = frc_tmp
  local trq_tmp = 0
  if stateA == 1 then trq_tmp = trq_tmp - 1 end
  if stateD == 1 then trq_tmp = trq_tmp + 1 end
  trq = trq_tmp
  print(frc)
  physics.set("relativeForce", Vector(0, 0, frc * -40))
  physics.set("relativeTorque", Vector(0, trq * 40, 0))
  print(physics.get("relativeForce"))
end

function onScriptingButtonUp(index, color)
  obj = self.getChild("Warthog(Clone)")
  nod = obj.getChild("Camera_Node")
  cam = nod.getComponent("Camera")
  isdrivemode = cam.get("enabled")
  physics = obj.getComponent("ConstantForce")
  print(index .. " " .. color .. " " .. tostring(isdrivemode))
  if index == 1 then stateW = 0 end
  if index == 2 then stateA = 0 end
  if index == 3 then stateS = 0 end
  if index == 4 then stateD = 0 end
  local frc_tmp = 0
  if stateW == 1 then frc_tmp = frc_tmp + 1 end
  if stateS == 1 then frc_tmp = frc_tmp - 1 end
  frc = frc_tmp
  local trq_tmp = 0
  if stateA == 1 then trq_tmp = trq_tmp - 1 end
  if stateD == 1 then trq_tmp = trq_tmp + 1 end
  trq = trq_tmp
  print(frc)
  physics.set("relativeForce", Vector(0, 0, frc * -40))
  physics.set("relativeTorque", Vector(0, trq * 40, 0))
  print(physics.get("relativeForce"))
end