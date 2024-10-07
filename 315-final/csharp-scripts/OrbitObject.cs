using UnityEngine;

public class OrbitObject : MonoBehaviour
{
    public Transform centerObject; // The object the moon will orbit around (Earth)
    public float orbitSpeed = 10f; // Speed of orbit
    public float orbitDistance = 5f; // Distance from the centerObject

    void Update()
    {
        if (centerObject != null)
        {
            // Keep the moon at a fixed distance from the Earth
            transform.position = centerObject.position + (transform.position - centerObject.position).normalized * orbitDistance;

            // Rotate the moon around the Earth
            transform.RotateAround(centerObject.position, Vector3.up, orbitSpeed * Time.deltaTime);
        }
    }
}
