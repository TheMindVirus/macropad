using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using UnityEngine;
using TMPro;

public class MacropadControl : MonoBehaviour
{
    private Ray ray;
    private RaycastHit hit;
    private float axis;
    private float delta;
    private float sensitivity;
    private Touch touch;
    private Vector3 origin;
    private Vector3 cursor;
    private bool selected;
    private bool first;
    private GameObject control;
    private Dictionary<string, Vector3> origins;
    private TextMeshProUGUI SevenSegment;

    [DllImport("__Internal")]
    private static extern void _SendMessage(int id, int msg, int x, int y);

    void Start()
    {
        hit = new RaycastHit();
        ray = new Ray();
        delta = 0.0f;
        sensitivity = 0.1f;
        touch = new Touch();
        origin = new Vector3(0.0f, 0.0f, 0.0f);
        cursor = new Vector3(0.0f, 0.0f, 0.0f);
        selected = false;
        first = true;
        control = null;
        origins = new Dictionary<string, Vector3>();
        SevenSegment = GameObject.Find("/Node-macropad_dot_io/Screen/Canvas/Text (TMP)").gameObject.GetComponent<TextMeshProUGUI>();

        Transform knob = GameObject.Find("/Node-macropad_dot_io/Knob0").transform;
        knob.eulerAngles = new Vector3(knob.eulerAngles.x, knob.eulerAngles.y - 20.0f, knob.eulerAngles.z);
        //Debug.Log(knob.eulerAngles);
        int value = (int)(((160.0f + (knob.eulerAngles.y - origin.y)) / 320.0f) * 127.0f); //Get Position
        if (value >= 0x8E) { value -= 0x8E; }
        SevenSegment.SetText(value.ToString());
    }

    void Update()
    {
        cursor = new Vector3(Input.mousePosition.x / Screen.width,
                             Input.mousePosition.y / Screen.height, 0.0f);
        InputMethod(Input.GetMouseButton(0), Input.GetAxis("Mouse Y"), cursor);

        for (int i = 0; i < Input.touchCount; ++i)
        {
            touch = Input.GetTouch(i);
            selected = (touch.phase != TouchPhase.Ended) && (touch.phase != TouchPhase.Canceled);
            cursor = new Vector3(touch.position.x / Screen.width,
                             touch.position.y / Screen.height, 0.0f);
            InputMethod(selected, touch.deltaPosition.y, touch.position);
        }
    }

    void InputMethod(bool Selected, float Axis, Vector3 Cursor)
    {
        //Debug.Log(cursor);
        ray = Camera.main.ViewportPointToRay(Cursor);
        if (Physics.Raycast(ray, out hit) && (!selected))
        {
            control = hit.collider.transform.gameObject;
            //Debug.Log(control.name);
        }
        if (control != null) //Support a variety of control classes here
        {
            if (Selected)
            {
                if (control.name.StartsWith("Button"))
                {
                    if (first)
                    {
                        if (!(origins.TryGetValue(control.name, out origin)))
                        {
                            origin = control.transform.position;
                            origins.Add(control.name, origin);
                        }
                        control.transform.position = new Vector3(origin.x, origin.y - 10.0f, origin.z);
                        int cc = 0;
                        int.TryParse(control.name.Substring("Button".Length), out cc);
                        _SendMessage(1, 0xB0, cc, 0x7F);
                    }                    
                }
                if (control.name.StartsWith("Knob"))
                {
                    if (first)
                    {
                        if (!(origins.TryGetValue(control.name, out origin)))
                        {
                            origin = control.transform.eulerAngles;
                            origins.Add(control.name, origin);
                            delta = origin.y;
                        }
                        else { delta = control.transform.eulerAngles.y - 180.0f; if (delta > 180.0f) { delta -= 360.0f; } } //- origin.y
                    }
                    var prev = control.transform.eulerAngles;
                    delta += (Axis * sensitivity * 120.0f);
                    control.transform.eulerAngles = new Vector3(origin.x, Mathf.Clamp(origin.y + delta, origin.y - 160.0f, origin.y + 160.0f), origin.z);
                    if (control.transform.eulerAngles != prev)
                    {
                        int cc = 0;
                        int value = (int)(((160.0f + (control.transform.eulerAngles.y - origin.y)) / 320.0f) * 127.0f); //Get Position
                        if (value >= 0x8E) { value -= 0x8E; }
                        SevenSegment.SetText(value.ToString());
                        _SendMessage(1, 0xB0, cc, value);
                    }
                }
                first = false;
            }
            if (!Selected)
            {
                if (control.name.StartsWith("Button"))
                {
                    var prev = control.transform.position;
                    if (origins.TryGetValue(control.name, out origin)) { control.transform.position = origin; }
                    if (control.transform.position != prev)
                    {
                        int cc = 0;
                        int.TryParse(control.name.Substring("Button".Length), out cc);
                        _SendMessage(1, 0xB0, cc, 0x00);
                    }
                }
                delta = 0.0f;
                first = true;
            }
        }
    }

    public void Acknowledge(int ACK)
    {
        int id = (ACK) & 0xFF;
        int msg = (ACK >> 8) & 0xFF;
        int x = (ACK >> 16) & 0xFF;
        int y = (ACK >> 24) & 0xFF;
        Debug.Log("[ACK]: [" + id.ToString("X2") + ", " + msg.ToString("X2") + ", " + x.ToString("X2") + ", " + y.ToString("X2") + "]");
    }
}
